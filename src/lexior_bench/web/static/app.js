"use strict";

/* ---- dynamic item rows (task create/edit forms) ---- */
const LexiorItems = {
  labels() {
    const area = document.getElementById("labels");
    if (area) return area.value.split("\n").map(s => s.trim()).filter(Boolean);
    return null; // task_detail provides labels via data attribute instead
  },
  addRow(split, labels) {
    const table = document.querySelector(`table.items[data-split="${split}"] tbody`);
    if (!table) return;
    const button = document.querySelector(`button.add-row[data-split="${split}"]`);
    const labelList = labels || this.labels() ||
      JSON.parse((button && button.dataset.labels) || "[]");
    const row = document.createElement("tr");
    const options = labelList.map(l => `<option value="${l}">${l}</option>`).join("");
    row.innerHTML = `
      <td><input name="${split}_index" value="${table.children.length}" size="4"></td>
      <td><textarea name="${split}_text" rows="2"></textarea></td>
      <td><select name="${split}_answer">${options}</select></td>
      <td><button type="button" class="remove-row">✕</button></td>`;
    table.appendChild(row);
  },
  refreshSelects() {
    const labelList = this.labels();
    if (!labelList) return;
    document.querySelectorAll("table.items select").forEach(select => {
      const current = select.value;
      select.innerHTML = labelList.map(l => `<option value="${l}">${l}</option>`).join("");
      if (labelList.includes(current)) select.value = current;
    });
  },
};

document.addEventListener("click", event => {
  if (event.target.matches("button.add-row")) {
    LexiorItems.addRow(event.target.dataset.split);
  }
  if (event.target.matches("button.remove-row")) {
    event.target.closest("tr").remove();
  }
});
document.addEventListener("input", event => {
  if (event.target.id === "labels") LexiorItems.refreshSelects();
});

/* ---- run page ---- */
function pollRunStatus() {
  const progress = document.getElementById("run-progress");
  if (!progress) return;
  fetch("/api/run/status").then(r => r.json()).then(job => {
    if (job.status === "running") {
      progress.hidden = false;
      document.getElementById("run-form").hidden = true;
      document.getElementById("run-bar").value = job.total ? (100 * job.done / job.total) : 0;
      document.getElementById("run-count").textContent = `${job.done} / ${job.total}`;
      document.getElementById("run-current").textContent = job.current || "";
      const errorLine = document.getElementById("run-errors");
      errorLine.hidden = !job.errors;
      if (job.errors) errorLine.textContent = `${job.errors} ⚠`;
      setTimeout(pollRunStatus, 1000);
    } else if (job.status === "done" || job.status === "error") {
      progress.hidden = true;
      const done = document.getElementById("run-done");
      done.hidden = false;
      const link = document.getElementById("run-results-link");
      if (job.run_id) link.href = `/runs/${job.run_id}`; else link.hidden = true;
      if (job.status === "error") {
        const errorText = document.getElementById("run-done-error");
        errorText.hidden = false;
        errorText.textContent = job.error || "error";
        document.getElementById("run-done-title").textContent =
          document.querySelector("[data-msg-failed]").dataset.msgFailed;
      } else if (job.errors) {
        const warn = document.getElementById("run-done-warn");
        warn.hidden = false;
        warn.textContent = `${job.errors}/${job.total} ${warn.dataset.msg}`;
      }
    }
  }).catch(() => setTimeout(pollRunStatus, 2000));
}

document.addEventListener("DOMContentLoaded", () => {
  const allTasks = document.getElementById("all-tasks");
  if (allTasks) {
    allTasks.addEventListener("change", () => {
      document.querySelectorAll(".task-check").forEach(box => {
        box.disabled = allTasks.checked;
        if (allTasks.checked) box.checked = true;
      });
    });
  }
  const start = document.getElementById("start-run");
  if (start) {
    start.addEventListener("click", () => {
      const models = [...document.querySelectorAll(".model-check:checked")].map(b => b.value);
      document.getElementById("extra-models").value.split("\n")
        .map(s => s.trim()).filter(Boolean).forEach(m => models.push(m));
      const tasks = [...document.querySelectorAll(".task-check:checked")].map(b => b.value);
      const errorLine = document.getElementById("run-error");
      errorLine.hidden = true;
      if (!models.length) { errorLine.textContent = start.dataset.msgNoModels; errorLine.hidden = false; return; }
      if (!tasks.length) { errorLine.textContent = start.dataset.msgNoTasks; errorLine.hidden = false; return; }
      fetch("/api/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          models, tasks,
          limit: document.getElementById("limit").value || null,
          max_tokens: document.getElementById("max-tokens").value || 512,
        }),
      }).then(async r => {
        if (r.status === 409) { errorLine.textContent = start.dataset.msgBusy; errorLine.hidden = false; return; }
        if (!r.ok) { errorLine.textContent = (await r.json()).error; errorLine.hidden = false; return; }
        document.getElementById("run-form").hidden = true;
        document.getElementById("run-progress").hidden = false;
        pollRunStatus();
      });
    });
  }
  if (document.getElementById("run-progress") &&
      document.getElementById("run-progress").dataset.running === "1") {
    pollRunStatus();
  }
});

/* ---- annotation page ---- */
document.addEventListener("click", event => {
  if (!event.target.matches(".annotate-btn")) return;
  const button = event.target;
  const action = button.dataset.action;
  if (action === "apply" && !confirm(button.dataset.confirm)) return;
  const row = button.closest("tr");
  const task = row.dataset.task;
  const provider = document.getElementById("annotate-provider").value;
  const out = row.querySelector(".annotate-result");
  const msg = out.dataset;
  out.hidden = false;
  out.textContent = "…";
  const url = action === "push" ? "/api/annotate/push" : "/api/annotate/pull";
  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ provider, task, dry_run: action === "preview" }),
  }).then(async r => {
    const data = await r.json();
    if (!r.ok) { out.innerHTML = `<span class="error">${data.error}</span>`; return; }
    if (action === "push") { out.textContent = `${data.pushed} ${msg.msgPushed}`; return; }
    const labelFor = { corrected: msg.msgCorrected, rejected: msg.msgRejected, invalid_correction: msg.msgInvalid };
    let html = `${data.annotated} ${msg.msgAnnotated} · ${data.validated} ${msg.msgValidated} · ${data.changes.length} ${msg.msgChanges}`;
    if (data.changes.length) {
      html += "<table><tbody>" + data.changes.map(c =>
        `<tr><td>${c.split}/${c.index}</td><td>${labelFor[c.action] || c.action}</td>` +
        `<td>${c.old ?? ""}${c.new ? " → " + c.new : ""}</td></tr>`).join("") + "</tbody></table>";
    }
    if (action === "apply") html += `<p class="success">${data.changes.length ? msg.msgApplied : msg.msgNothing}</p>`;
    out.innerHTML = html;
  }).catch(error => { out.innerHTML = `<span class="error">${error}</span>`; });
});
