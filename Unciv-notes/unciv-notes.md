#### UI
* Yes/No boxes and keys Y, N, Enter - i10n?
    * branch: [YesNoPopupKeys](https://github.com/SomeTroglodyte/Unciv/tree/YesNoPopupKeys)
* World view - Keys: U = Overview units, C = Overview cities, T = Overview trades, R = Overview resources, V = Victory screen
* Overview cities and units retain scroll position, ?Overview itself retains selected tab?
* Remap Improvement "R" key to railroad once researched
* Mousewheel in mod manager
* F1 key to civilopedia
    * branch: [LinkableCivilopedia1](https://github.com/SomeTroglodyte/Unciv/tree/LinkableCivilopedia1)

#### Shortcuts
* Buying several tiles in city view (buy next ring?)
* Buying buildings faster in city view (buy all affordable? buy queue?)
* Global city construction changes (e.g. all science to gold) -> overview-cities
* Upgrade all units command in overview-unit

#### Debug
* Incompatibility More luxuries mod + 5Hex tileset + experimental tile layering: coral+fisheries, barrier reef black
* Pillage / rebuild "city center"
    * seen tiles w/rebuildable ccenter in enemy territory -> the AI does it too
    * review what razing cities code does with improvements
* review what razing cities code does with tile ownership - transfer tiles in 5t zone of another city to that city? Even if not connected to tiles already owned by that city? Citadels? Need to know original Civ5 behaviour
* Multiturn movement ETA off, or circles promising tiles reachable this turn that aren't (rivers? cannot be only trigger)

#### Try
* ~~Higher resolution option - 1800 looks good on a 2.5k 32" panel, but not much better than 1500. 2400 looks worse.~~

#### Civilopedia
* "Link right half" - make it callable to preselect a specific entry
    * branch: [LinkableCivilopedia1](https://github.com/SomeTroglodyte/Unciv/tree/LinkableCivilopedia1)
* "Link left half" - system to make partial text selectable
* "Internal Link generation" - criteria? Some extra metadata needed?
    * Only way I see: Find unused bracket pair, *declare* as containing category:entry for civilopedia
    * Make toLabel remove the marker and generate an onClick instead
    * Modify known/linkworthy multiline labels to split and convert to multi-label table
* "External links" - e.g. world view bottom right: terrain, resource, improvement, unit?
    * TileInfoTable (right just above minimap) - gets text from tile.toString so it's no easier than internal links
* System to include extra text for hardcoded stuff:
    * ~~Citadel limitation 'within or next to own borders'~~ - no longer an example
    * A/C ruins, city center, barbarians
    * Effect of roads/railroad
    * "Remove" actions
    * Great person improvements - "can only be built by"
* new category UI help including screenshots of world view / city explaining parts

#### Ideas
* Workable city radius moddable (hardcoded to 3 in CityInfo.setTransients)
