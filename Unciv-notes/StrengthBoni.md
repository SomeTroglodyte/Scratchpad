|placeholder|Att/Def|Unit/Civ|suggested|notes|
|-----------|-------|--------|---------|-----|
|+[]% Strength vs []|*|U,C|[]% Strength vs []|isProbablySiegeUnit will need to check param0 when this is generalized|
|-[]% Strength vs []|*|U,C|-|see above|
|+[]% Combat Strength|*|U|[]% Combat Strength||
|[] units deal +[]% damage|*|C|[] units deal []% damage||
|+[]% Strength when attacking|*|U|[]% Strength when attacking||
|Bonus for units in 2 tile radius 15%|*|U|Bonus for units in [] tile radius []%|modChecker should ensure param1 in 1..5|
|[]% Strength when stacked with []|*|U|OK|implementation should check if a mod makes param1 apply to the unit itself|
|[]% Strength for [] units which have another [] unit in an adjacent tile|*|C|OK||
|[]% Strength for enemy [] units in adjacent [] tiles|*|U|OK||
|+10% Strength for all units during Golden Age|*|C|[]% Strength for all units during Golden Age||
|+30% Strength when fighting City-State units and cities|*|C|[]% Strength when fighting City-State units and cities||
|+[]% Strength in []|*|U|[]% Strength in []|tileFilter for defender's tile|
|+[]% Strength for units fighting in []|*|C|[]% Strength for units fighting in []|tileFilter for defender's tile|
|+[]% Strength if within [] tiles of a []|*|C|[]% Strength if within [] tiles of a []|tileFilter for defender's tile|
|+[]% attack strength to all [] units for [] turns|A|C|[]% attack strength to all [] units for [] turns||
|+15% Combat Strength for all units when attacking Cities|A|C|[]% Combat Strength for all units when attacking [cityFilter]||
|+[]% attacking strength for cities with garrisoned units|A|City|[]% attacking strength for [cityFilter] with garrisoned units||
|[]% attacking Strength for cities|A|City|[]% Offensive Strength for [cityFilter]|for consistency with "Defensive"|
|+[]% Strength when defending|D|U|[]% Strength when defending||
|[]% Strength when defending vs [] units|D|U|OK||
|+[]% Defensive strength for cities|D|City|[]% Defensive strength for [cityFilter]||
|Defense bonus when embarked|D|U|Defence bonus when embarked|Works exactly like the next one - but display wording|
|Embarked units can defend themselves|D|C|OK||
|+[]% defence in [] tiles|D|U|[]% defence in [] tiles|not in `getTileSpecificModifiers`?|



Hardcoded values (Ideas how to achieve moddability?):
- Great General effect = +15
- Missing Resource = -25
- Landing = -50
- Across river = -20
- Flanking = 10 * (numberOfAttackersSurroundingDefender - 1)
- Embarked + (Defense bonus when embarked | Embarked units can defend themselves) = 100
- Wounded = 1 - (100 - combatant.getHealth()) / 300f

Not counting:
- Already deprecated
- Fortification

Additional considerations:
- Defense/Defence: I would prefer defense, but Unciv genereally tends to yankee spelling where a difference exists. Consistency is more important than cowboy/python preferences.
- Do we want more consistency "Strength" / "Combat strength" or is variety a nice thing in this case?
- We need a generic interface abstraction for uniques/uniqueObjects. Definitely.
- Some uniques specific to "U" Units could work for cities as well. Haven't checked whether they already do due to "Unit" actually being an ICombatant - does that interface abstract uniques?
- All uniques in `getTileSpecificModifiers` always check the _defender_'s tile. I've marked them in the table.
- We would need tile-specific modifiers using the attacker's tile for #4508. I'd code them outside `getTileSpecificModifiers` and comment why. Question is - which one / unique text wording?
- Wording of the 'reason'  (key in modifiers map) - any where a clearer one were desirable? (e.g. what once was "Haka War Dance: -10%" is now "Adjacent enemy units: -10%")
