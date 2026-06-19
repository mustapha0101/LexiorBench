## Purpose
Verify whether a bibliographic reference matches the legal source cited, using McGill Guide format (10th ed.).

## Question format
Input: a citation string paired with a description of the source.
Output: `Oui` (citation is correct) | `Non` (citation has an error)

**Example:**
> "Citation proposée: 'Doré c Barreau du Québec, 2012 CSC 12, [2012] 1 RCS 395.' — Cette citation correspond-elle à l'arrêt portant sur le contrôle judiciaire des décisions du Barreau?"
> → Oui

## Positive — `Oui`
- Citation format matches McGill Guide: parties, year, neutral citation, reporter citation
- Year, volume, reporter, and page are all correct

## Positive — `Non`
- Wrong year (e.g., 2011 instead of 2012)
- Wrong neutral citation number
- Wrong reporter (e.g., RCS vs CF)
- Parties listed in wrong order (respondent before applicant)
- Missing required element

## Legal sources
- McGill Guide to Legal Citation, 10th ed. (Le Manuel canadien de la référence juridique)
- CanLII neutral citations for CSC, CA-QC, Cour fédérale, Cour du Québec
- Key landmark cases: Doré, Dunsmuir, Vavilov, Clements, Jordan

## Diversity guidelines
- Include citations to: CSC, CA-QC, Cour fédérale, Cour du Québec, CRTC, TAL
- Mix errors: wrong year, transposed neutral citation number, wrong reporter
- Include both English and French case names
- Include legislation citations (LIR, CCQ, LPC) not just case law

## Do not use
- Bluebook format (US)
- OSCOLA (UK)
- Invented case names that do not exist in CanLII