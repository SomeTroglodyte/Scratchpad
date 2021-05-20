Follow Yair's guidelines, of course - but this file is for specific things I stumbled upon.

## IDE automatical or semi-automatical import directives
Sometimes you use a class for the first time in a source file - e.g. something used only a few Gdx `Table`s
and now you want to pass a reference as generic `Actor` - you type it and it is colored red, the quick-fix offers to import it for you.
In such cases, please double check the qualifiers of the possibly long list of offered imports - is it Java's `math.min` or Kotlin's `math.min`
(in this example, it's important to always prefer Kotlin libraries, see [this fix](https://github.com/yairm210/Unciv/commit/984293c2522e70ff56f46b1443fbf7286d9f7ff7#commitcomment-51068974) ).

## Suppressing warnings
Warnings are a complex subject matter, here I'll just note this: The correct @Suppress annotation _is_ offered in quick-fixes by 
Android Studio, but on the second level. Even if the only menu entry says `delete` - open the little trangle.

## Kdoc
I've gradually come to the resolution that all public classes, properties and methods I create (or modify and understand) get complete documentation on the `/** .. */` format - this results in very helpful tooltips everywhere these elements are used. You can see them immediately (unless your indexer is way behind).

The reference is [here](https://kotlinlang.org/docs/kotlin-doc.html).

A not-quite-obvious trick: To link to something not known in the current file use the full path including package:
`[OptionsPopup]` would not work if not imported, `[com.unciv.ui.worldscreen.mainmenu.OptionsPopup]` would, but `[OptionsPopup][com.unciv.ui.worldscreen.mainmenu.OptionsPopup]` gives the friendliest result.
