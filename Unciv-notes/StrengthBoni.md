
|placeholder|Att/Def|Unit/Civ|suggested|notes|
|-----------|-------|--------|---------|-----|

|+[]% Strength vs []|*|U,C|isProbablySiegeUnit will need to check param0 when this is generalized|
|-[]% Strength vs []|*|U,C|
|+[]% Combat Strength|*|U|
|[] units deal +[]% damage|*|C|
|+[]% Strength when attacking|A|U|
|+[]% attack strength to all [] units for [] turns|A|C|
|+15% Combat Strength for all units when attacking Cities|A|C|
|+[]% attacking strength for cities with garrisoned units|A|*|
|[]% attacking Strength for cities|A|*|
|+[]% Strength when defending|
|[]% Strength when defending vs [] units|
|+[]% defence in [] tiles|||"defense"|
|Bonus for units in 2 tile radius 15%|*|U|
|[]% Strength when stacked with []|*|U|implementation should check if a mod makes param1 apply to the unit itself|
|[]% Strength for [] units which have another [] unit in an adjacent tile|*|C|
|[]% Strength for enemy [] units in adjacent [] tiles|*|U|
|+[]% Defensive strength for cities|
|+10% Strength for all units during Golden Age|*|C|
|+30% Strength when fighting City-State units and cities|*|C|

Hardcoded values
- Great General effect = +15
- Missing Resource = -25
- Landing = -50
- Across river = -20
- Flanking = 10 * (numberOfAttackersSurroundingDefender - 1)
- Embarked + (Defense bonus when embarked | Embarked units can defend themselves) = 100
