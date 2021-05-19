#### UI
* Yes/No boxes and keys Y, N, Enter
    * ~~branch: [YesNoPopupKeys](https://github.com/SomeTroglodyte/Unciv/tree/YesNoPopupKeys)~~
    * ~~Needs rethink: generic keyhandler for Popup class?~~
    * local branch ready
* ~~World view - Keys: U = Overview units, C = Overview cities, T = Overview trades, R = Overview resources, V = Victory screen~~
* Overview cities and units retain scroll position, ~~Overview itself retains selected tab~~ -> local branch
* ~~Remap Improvement "R" key to railroad once researched~~
* Mousewheel in mod manager
* ~~F1 key to civilopedia~~
* Do not offer Sleep until healed when healing==0 (marine -> `MapUnit.rankTileForHealing`)
    * Check: Is marine supply promotion Vanilla Civ5?
* Popups with only a 'close' button dismissable with keyboard
* Wrapper class for Popups with only text and one or two buttons: "InfoPopup"
* Internationalization of keyboard shortcuts???
* Help in the Improvement Picker: 'research X to enable Y'
* Finally check when and how map generation choices are persisted and when not

#### Shortcuts
* ~~Buying several tiles in city view (buy next ring?)~~ -> PR
* Buying buildings faster in city view (buy all affordable? buy queue?) -> local branch
* Global city construction changes (e.g. all science to gold) -> overview-cities
* Upgrade all units command in overview-unit

#### Debug
* ~~Incompatibility More luxuries mod + 5Hex tileset + experimental tile layering: coral+fisheries, barrier reef black~~
* ~~Pillage / rebuild "city center"~~
    * ~~seen tiles w/rebuildable center in enemy territory -> the AI does it too~~
    * ~~review what razing cities code does with improvements~~
* ~~review what razing cities code does with tile ownership - transfer tiles in 5t zone of another city to that city? Even if not connected to tiles already owned by that city? Citadels? Need to know original Civ5 behaviour~~
* Multiturn movement ETA off, or circles promising tiles reachable this turn that aren't (rivers? cannot be only trigger)
* Connect to capital / rivers / engineering not researched
* Legalism + captured cities / rebellion: I still think this is wrong as it is now, and it forces unintentionally to choose a construction for cities that do not construct

#### Try
* ~~Higher resolution option - 1800 looks good on a 2.5k 32" panel, but not much better than 1500. 2400 looks worse.~~

#### Civilopedia
* branch: [Civilopedia-Flavour](https://github.com/SomeTroglodyte/Unciv/tree/Civilopedia-Flavour)
* ~~"Link right half" - make it callable to preselect a specific entry~~
* ~~"Link left half" - system to make partial text selectable~~
* ~~"Internal Link generation" - criteria? Some extra metadata needed?~~
    * ~~Only way I see: Find unused bracket pair, *declare* as containing category:entry for civilopedia~~
    * ~~Make toLabel remove the marker and generate an onClick instead~~
    * ~~Modify known/linkworthy multiline labels to split and convert to multi-label table~~
* ~~"External links" - e.g. world view bottom right: terrain, resource, improvement, unit?~~
    * ~~TileInfoTable (right just above minimap) - gets text from tile.toString so it's no easier than internal links~~
* ~~System to include extra text for hardcoded stuff:~~
    * ~~Citadel limitation 'within or next to own borders'~~ - no longer an example
    * A/C ruins, city center, barbarians
    * Effect of roads/railroad
    * "Remove" actions
    * ~~Great person improvements - "can only be built by"~~
* ~~Nation display: Unique TileImprovement `terrainsCanBeBuiltOn` not displayed~~
* ~~Nation display: LeaderPortrait~~
* ~~new category UI help including screenshots of world view / city explaining parts~~
* Entry for "Terrain" rivers?
* Terrain image creation is standalone but MapEditorOptionsTable uses the same code distributed over addTerrainOptions loop head and makeTileGroup

#### Ideas
* Workable city radius moddable (hardcoded to 3 in CityInfo.setTransients)
* Some more statistics like %world explored, avg battles per turn worldwide, % of worldwide battles participated in, %of battles won/lost/survived, +/- units captured,...
