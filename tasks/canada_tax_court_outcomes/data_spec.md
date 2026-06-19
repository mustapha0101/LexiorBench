## Purpose
Classify whether a Tax Court of Canada decision excerpt reveals the outcome of the appeal (allowed / dismissed / other).

## Question format
Input: excerpt from a Tax Court of Canada judgment (English or French).
Output: `allowed` | `dismissed` | `other`

**Example:**
> "L'appel est accueilli en partie et le dossier est renvoyé au ministre pour réévaluation."
> → allowed

## Positive — `allowed`
- Excerpt explicitly states the appeal is allowed, granted, or partially allowed
- Mixed results (partly allowed, partly dismissed) → classify as `allowed`
- Costs orders alone are not the outcome; ignore them

## Positive — `dismissed`
- Excerpt states the appeal is dismissed, rejected, or denied

## Positive — `other`
- Outcome is unclear, interlocutory, procedural, or not stated in the excerpt
- Excerpt is from reasons only, no dispositif present

## Legal sources
- Tax Court of Canada Act, RSC 1985 c T-2
- Real Tax Court decisions from CanLII (taxe.ca, canlii.org — Tax Court of Canada section)
- Bilingual: include both English and French decision excerpts

## Diversity guidelines
- Mix English and French excerpts (federal bilingual court)
- Vary excerpt location: dispositif, opening paragraph, summary
- Include both income tax and GST/HST cases
- Include cases where the outcome is buried in a long paragraph (hard negatives)

## Do not use
- US Tax Court decisions
- Provincial tax tribunal decisions
- Excerpts that only discuss procedure with no outcome signal