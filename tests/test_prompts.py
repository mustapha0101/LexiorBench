from lexior_bench.prompts import render_examples, render_prompt


def test_render_examples_blocks(toy_task):
    block = render_examples(toy_task)
    assert block == (
        "Situation : Le ciel est bleu.\nRéponse : Vrai"
        "\n\n"
        "Situation : La mer est rose.\nRéponse : Faux"
    )


def test_render_prompt_few_shot(toy_task):
    prompt = render_prompt(toy_task, "L'eau bout à 100 degrés.")
    assert "{{examples}}" not in prompt and "{{text}}" not in prompt
    assert "Situation : Le ciel est bleu.\nRéponse : Vrai" in prompt
    assert prompt.rstrip().endswith("Situation : L'eau bout à 100 degrés.\nRéponse :")


def test_render_prompt_pure_legalbench_passthrough(toy_task):
    toy_task.base_prompt = "Question : {{text}}\nRéponse :"
    prompt = render_prompt(toy_task, "Deux et deux font cinq.")
    assert prompt == "Question : Deux et deux font cinq.\nRéponse :"
    # no few-shot block injected
    assert "ciel" not in prompt
