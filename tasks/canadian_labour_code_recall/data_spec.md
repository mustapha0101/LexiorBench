## Purpose
True/False recall of rules under the Canada Labour Code (federal).

## Question format
Input: declarative statement about federally regulated workplace rules.
Output: `Vrai` | `Faux`

**Example:**
> "Le Code canadien du travail s'applique aux employeurs sous réglementation fédérale, comme les banques et les transporteurs aériens."
> → Vrai

## Positive — `Vrai`
- Accurately states a rule from Parts I (industrial relations), II (occupational health and safety), or III (labour standards) of the Code

## Positive — `Faux`
- Confuses federal Code with provincial labour laws (LNT for Quebec)
- States a rule that applies only to provincially regulated employers
- Misstates a threshold (e.g., wrong notice period, wrong overtime rate)

## Legal sources
- Canada Labour Code, RSC 1985 c L-2 (Parts I, II, III)
- Federal labour standards regulations
- CIRB and Federal Court decisions (CanLII)

## Diversity guidelines
- Cover: scope of application (which employers), termination notice, overtime, leave entitlements, collective bargaining, OHS duties
- Include difficult cases: interprovincial transport, broadcasting, Indigenous enterprises
- Mix Part I (unions), Part II (safety), Part III (individual standards) questions

## Do not use
- Quebec LNT rules
- Provincial occupational health codes