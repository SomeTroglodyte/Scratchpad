## Notes on working with your Unciv fork
So, I'll try my hand at documenting what I found to be useful.
This is related to Yair's [From code to deployment](https://github.com/yairm210/Unciv/wiki/From-code-to-deployment) but with a slightly different focus. This is geared to using Android Studio 4.2, specifically, for most tasks.

### Branches are important
* Remap ``Ctrl-Shift-` `` if you're not on a US keyboard. You'll need that git branches popup all the time. The other all-important keyboard shortcuts are `Ctrl-K` and `Ctrl-Shift-K`.
(It's under `File-Settings-Keymap-Version Control Systems-git-*Repository*`)
* ***Always*** work in a branch (other than master).
* Keep different matters in different branches and develop them independently. Switch using the branch-popup->checkout. Try to partition your branches in such a way as to include the least possible amount of changes that still work together and produce a playable game.
* Local changes to files, even if made outside Android Studio (useful!), become part of a branch when you commit. Checkouts apply commits to your local files. Creating a branch does nothing with your local files, so you can create a branch after coding the changes that should go into it, but I prefer always keeping the branch the current coding should go into active, so I create my branches before changing anything.
* Everything I said so far applies to local branches. The relationship of those to remote branches (which are visible on your github web page) is defined by Push or Pull operations.
* The simple way to publish a local branch when it is ready is to make sure no local changes are uncommitted, then Push, then go to your for on the web page, then create your Pull Request there. That's fully okay if you can be absolutely sure the files you touched have not been modified by someone else in the meantime - otherwise, you create more work for the boss when merging the PR. To pre-emptively help this, read [below](#keeping-your-fork-up-to-date)
* There's no reason to keep copies of the upstream non-master branches, so go ahead and delete them right after forking - or later.

### Keeping your fork up to date
This is not trivial and you can easily get lost, especially if you're used to Visual Studio/Azure DevOps, where terms like check out or branch simply mean different things than here. If you look at IntelliJ's [Contribute to projects on GitHub](https://www.jetbrains.com/help/idea/2021.1/contribute-to-projects.html), you can see not only do their instructions not match the environment, the video also nicely shows the pros get lost, too.

* Set up the original Unciv repo as remote:
`VCS->Git->Remotes`, little `plus` button, name e.g. "`yairm210/master`", URL "`https://github.com/yairm210/Unciv.git`", OK.

This needs to be done only once.

* Make sure your local master is marked current. If not, do a checkout.
* Always do `VCS->Git->Fetch` if you want to make sure your local IDE's knowledge is up to date with the world out on github. In my experience, this will not reliably show whether you are behind ([WIP](#wip)). Going to your fork on github will show a correct "This branch is X commits behind yairm210:master" message - the following pull/push procedure still applies.
* For a visual representation, hit `Alt-9` (not Alt-F9) to have the 'Git' tool pane open in the lower right (assuming you did not customize your IDE too far), then make sure that `Log` is selected on the upper edge of that tool's pane. See commit names and colored lines? Good. Look for the yellow tag, that's where you "are" relative to what your `fetched` set of `remotes` knows about commits.

So the goal now is to get that yellow tag to the top and the corresponding code into your online and local master branches ("master" and "origin/master" in your branches popup)

* I heard that 'VCS->Update Project' can help here but haven't so far understood what that does exactly.
* I use the 'explicit way' - first pull from `yairm210/master` using `VCS->Git->Pull`: select `yairm210/master` in the middle field, the right should already say `master`. Both mean the source of the pull, the destination is always the current branch. You can see where your current branch is: in the far lower right on the status bar, or lower left in the tree section of the git pane log tab, or using the branches popup beforehand. Do not select any modifiers for the pull. Do the `Pull`, and our yellow tag will move up, though not always all the way to the top - your yellow tag should now be the same row the purple "yairm210/master/master" tag is. Only the tag "yairm210/master/translations" should be above us - explanations welcome. If this is not the case, re-fetch and pull from yairm210/master again.

Now your local master branch is up to date, but the online copy "origin/master" is not yet, as you can see by the position of its purple tag.

* Do a push from your local master to the online master: `VCS->Git->Push` or `Ctrl-Shift-K`, make sure you're pushing `master→origin:master` and go. Note this is different from the pushes you do to prepare a PR - this is master to master, those are specific branch to online copy of specific branch. Note how your little purple tag symbol has moved.

I did an explicit check on the online fork at this point. Pushing your own contributions will pop a yellow background menu offering to create a PR as soon as you browse to your fork, but this updated-local-master -> online master push did not. Which is as it should be.

If you did all this without some contribution of your own waiting in a separate branch, you're done. If there is, read on.

### Locally merging a branch before creating a Pull Request from it
If your proposed contribution works and you have tested it, but have not recently synced with newer upstream commits, do so before pushing your new branch to your github fork. Follow the [Keeping your fork up to date](#keeping-your-fork-up-to-date) chapter above - paying attention to do so with your master branch. The state now is even worse than pushing and PR'ing without updating your master first, but after merging and re-testing it will be significantly better!

* So your master moved ahead of the branch your new contribution is in. In the git pane you can visualize this by selecting local master / your branch in the tree on the left and observing the commits list with the colourful lines. Your new branch is missing some commits master already knows about.
* Make sure your local master is still active/current (has the tag not the star, has no checkout in its context menu)
* From the git pane's branch tree or the branches popup, right click *on your new branch* and do a `Checkout and rebase onto current`. No messages or popups means your changes were compatible with all the commits you just moved forward (inluded in the base of your branch by rebasing), and you could go ahead and push the branch to your fork and go there to make a PR out of it. 

If merging needs action, the IDE will tell you so and guide you - the "Conflicts" window pops up. I suggest ignoring the two buttons "Accept Yours/Theirs", use "Merge" (unless it's a binary file or an atlas). This will pop up a diff for the selected file comparing your source code with your master (now in sync with the current upstream sources). You can choose yours or 'theirs' for every distinct change, and I'd recommend manually choosing for each of them - won't take long. Merge progress can be watched in the upper right corner. Once you have treated _all_ of the differences, a small notice will appear top center "All changes have been processed" - use the `save and..` link offered (wording differs depending on remaining work in other files).

You're now back to your normal work environment - now ***T E S T*** your merge result! This is critical - if you did need to resolve conflicts, then that means you will need to test both whether your new features/fixes still work as before; and read their commit notes and test whether their new features/fixes _also_ work.

Might add more details next time I experience it ([WIP](#wip)).

### Bringing a branch that already has a PR up to date
- Commit any recent changes of your local branch and push them. Several unpushed commits can be squashed, but do not use amend or squash with anything already pushed (squash is easiest from git history, don't forget to select your branch there).
- Check out master and update normally, including pushing it to your origin/master.
- Check out the work branch again
- In branch manager, use your `master` branch context menu, choose 'Merge into current'. Resolve conflicts - if in doubt or you know that you will have to redo the file anyway, choose 'Accept theirs' (e.g. for an atlas with its png - don't forget to regenerate those if they were the cause of a merge conflict).
- Push. The commit list and file diff shown by Android Studio will display stuff that isn't yours and which you do not want to be part of the PR, but so so anyway. Go to your PR on the web an check that those foreign changes are not displayed.
- Success!

### Testing another collaborator's work
You see a PR and want to test it? Actually, you can test _any_ branch of _any_ Unciv fork because the 'public' property is inherited. So all that is required is that the author pushed something he thinks works.
- Look up the repo in question, e.g. https://github.com/xxxxxx/Unciv, and get the 'clone' https link: Drop down the code menu, make sure the https tab is selected, copy the link. This may be identical to the repo link or end in '.git', whichever it is, take it as is.
- Go to VCS-git-remotes like described above (under "[Keeping your fork up to date](#keeping-your-fork-up-to-date)") and enter the link.
- Do a Git fetch and wait a short while. The other repo's branches should appear in your branch manager.
- Check out your `master` - or make sure your local changes are empty using any other method, like looking in the git log.
- Check out the branch in question directly like any other unless it is named identically to one of yours - e.g. they developed in `master`.
- If there is a branch name conflict, use the "New branch from selected..." entry from the context menu, right under checkout.
- Start the debugger and test away!

### Run Unciv unit tests
<sub>(thanks to <a href="https://github.com/xlenstra">@xlenstra</a> for helping me create this chapter)</sub>
- Edit run configurations as you did for your 'desktop' run config. Use Run / Edit Configurations or the dropdown where the existing ones are.
- Templates -> Gradle, top right -> Create configuration
- Give it a nice name, e.g. 'Unciv Unit Tests'
- Set 'Gradle project:' to 'Unciv'
- Set 'Tasks:' to ':tests:test'
- Set 'Arguments:' to `--tests "com.unciv.testing.*"`
- Save the config.
- That's it! You can now run it or even debug the tests with breakpoints and everything.

#### Run Unciv unit tests under JUnit (Android Studio 4.2.* or older)
- Edit run configurations as you did for your 'desktop' run config. Use Run / Edit Configurations or the dropdown where the existing ones are.
- Templates -> Android JUnit, top right -> Create configuration
- Give it a nice name, e.g. 'Unciv Unit Tests'
- Set 'Use classpath of module' to 'Unciv.tests'
- Set the working directory just as you did for the debug config. This is important, as tests cover the ruleset and translations.
- Set 'Test kind' to 'all in directory', directory = 'tests/src/com/unciv' relative to your clone's root - use the picker to make this path absolute.
- Save the config.
- That's it! You can now run it or even debug the tests with breakpoints and everything.

### Getting a *jar* from your branch
- Checkout the branch, verify it runs fine in the debugger.
- Open the terminal pane (little tab bottom left), `./gradlew desktop:dist` like described [here](https://github.com/yairm210/Unciv/wiki/Building-locally-without-Android-Studio).
    - terminal gradlew does not automatically use the same Java JRE as Studio-run Gradle. You may need to set JAVA_HOME (`export`).
    - On windows I use: `set "JAVA_HOME=C:\Program Files\Android\Android Studio\jre" & gradlew desktop:dist` - the box has _no_ system-wide Java.
- Look under ./desktop/build/libs (that terminal starts out in your project root) for the jar.
- I suggest you rename it to `Unciv-yourgithubname-branchname.jar` if you want to keep it or show it to someone.

### Getting a debug *apk* from your branch
- Checkout the branch, verify it runs fine in the debugger.
- Menu: Build - Build Bundle(s) / APK(s) -> Build APK(s)
- Look in event log for the 'locate' link or under ./android/build/outputs/apk/debug for your apk.
- I suggest you rename it to `Unciv-yourgithubname-branchname-debug.apk` if you want to keep it or show it to someone.

### Some more useful gradle commands
- `./gradlew desktop:clean core:clean android:clean server:clean tests:clean` clean code, force recompilation
- `./gradlew --warning-mode all --stack-trace --scan desktop:build` look for deprecated stuff in our build scripts to prepare for a gradle major upgrade (not sure this works!)
- Look in [buildAndDeploy.yml](https://github.com/yairm210/Unciv/blob/master/.github/workflows/buildAndDeploy.yml) for reference.
        - Packr prerequisites: Download [packr-all-4.0.0.jar](https://github.com/libgdx/packr/releases/download/4.0.0/packr-all-4.0.0.jar) to your project root (and add to .git/info/exclude!)
        - For Linux download [JRE 11.0.11_9](https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.11%2B9/OpenJDK11U-jre_x64_linux_hotspot_11.0.11_9.tar.gz) as `jre-linux-64.tar.gz` to your project root and exclude from git
        - For Win32 download [JRE 1.8.0.252 b09](https://github.com/ojdkbuild/ojdkbuild/releases/download/java-1.8.0-openjdk-1.8.0.252-2.b09-x86/java-1.8.0-openjdk-1.8.0.252-2.b09.ojdkbuild.windows.x86.zip) as `jdk-windows-32.zip` to your project root and exclude from git
        - For Win64 download [JRE 1.8.0.232 b09](https://github.com/ojdkbuild/ojdkbuild/releases/download/java-1.8.0-openjdk-1.8.0.232-1.b09/java-1.8.0-openjdk-1.8.0.232-1.b09.ojdkbuild.windows.x86_64.zip) as `jdk-windows-64.zip` to your project root and exclude from git
        - Linux bundle: `./gradlew desktop:packrLinux64 desktop:zipLinuxFilesForJar`
        - Windows bundle: `./gradlew desktop:packrWindows64 desktop:packrWindows32`
        - Mac bundle: `./gradlew desktop:packrMacOS`
        - Results from packr are placed in /deploy

### WIP
* **Work in Progress**

Any help welcome!
