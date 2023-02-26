## Comments on Unciv "[Getting Started](https://github.com/yairm210/Unciv/wiki/Getting-Started)"
Specific to a fresh installation on Mint 20.1 (ubuntu 20.04 focal)

### Android Studio
I do the install from the [maarten-fonville PPA](http://ppa.launchpad.net/maarten-fonville/android-studio).

Pay attention to versions (the PPA offers betas) - if in doubt google first. The shell snippets below show how I chose 4.2 over 4.1 - this got me a beta which then self-updated to a RC1, and which suggested a SDK unsuitable for Unciv, but in the end was just fine.

Setting up Android Studio will download at least one SDK - make sure you get the one Unciv specifies (as of 2023-02 that is API level 32 matching Android 12L "Sv2"), Unciv will not build against a different API level SDK. The required API can be looked up in the file [android/build.gradle.kts](https://github.com/yairm210/Unciv/blob/master/android/build.gradle.kts) - check compileSdk and targetSdk lines.

Do an update check from within Android Studio immediately, also for SDK tools, SDK and plugins. Updating Android Studio itself requires root, so run it under sudo as shown below, but do not allow it to dowload any optional components in that context - cancel everything until you get to the small intro menu, then bottom-right `Configure->Check for Updates`. When that is done, restart under your normal user and in the same place, no project loaded yet, go to `Configure->Settings->Appearance & Behaviour->System Settings->Android SDK` and check the Status column on the `SDK Platforms` *and* `SDK Tools` tabs and update as applicable (while there also check the build tools issue below), then in the same window go to `Plugins` from the left menu, and check the Kotlin plugin for an update. I'd also suggest going to `Settings->Appearance & Behaviour->System Settings->Memory Settings` and increasing the IDE max heap size if you got RAM to spare.

##### Terminal commands - *do not execute everything blindly*
```bash
# New software source - can be removed from update manager
sudo apt-add-repository ppa:maarten-fonville/android-studio
# Refresh software lsit
sudo apt update
# Check out which packages are available - look only at the "Note, selecting" lines (or just below those whether one is already installed)
sudo apt install android-studio-* -s
# Now choose from the offered versions and install one of them
sudo apt install git android-studio-4.2 -y
# Run with root rights to self-update - cancel all import settings/download SDK/etc and quit immediately after
sudo /opt/android-studio/bin/studio.sh
```

### The build tools issue
Since gradle 7 an on-demand load of SDK Build tools fails (you'll know when you see something mentioning `ZipFile.<init>(java.nio.channels.SeekableByteChannel)`). Therefore you need to pre-install the exact expected version yourself. As of 2023-02 that is 32.0.0, not dictated by a project config file (but it could be), but by the gradle version. It is also mentioned in the logs of builds failing for that reason. No version automatically installed and updated would work at this point.

To download a specific version, in most cases you **will** need to check the "Show Package Details" checkbox well-hidden in the SDK manager.

### Java JDK
The Ubuntu 20.04 default JRE is an OpenJDK 11 variant with a bug rendering it unable to run Unciv (and other Gdx games; see also [#3770](https://github.com/yairm210/Unciv/issues/3770)). Just installing Android Studio will change the system to use a ubuntu-supplied OpenJDK 14 (full JDK) as default java, and this one boasts the same bug. But it also brought along a separate OpenJDK 11 version not known to `apt` or `update-alternatives` which works - in my case located at `/opt/android-studio/jbr`.

After cloning your fork into Android Studio, I'd suggest you immediately check its JDK settings and change it to use said bundled JDK - with a different one you might get [gradle errors](https://duckduckgo.com/?q="org.codehaus.groovy.control.MultipleCompilationErrorsException") or the ubuntu bug. `File->Project Structure->SDK Location`, field `JDK location`. Just ensure the first option from the dropdown named `Embedded...` is selected - in my case it was not for whatever reason.

If you did need to change the project JDK, thanks to gradle having already run unasked, you might get a stale cache - if you see an unsuccessful gradle build at first, look for the well-hidden `File/Invalidate Caches` command.

#### Adoptium JDKs

Instead of preferring the Studio-bundled JDK, you can opt for more current JDK's from adoptium.net. The archives the site offers to download are just the files without installer, and they work as long as you manage how they're called yourself. But... You can also install them via `apt`, and then `update-alternatives` will work just fine. You can run IDE, Gradle and debugger under the same JDK 17. Duckducked how-tos may suggest configuring the source using `/etc/os-release` - this will **NOT** work on mint, that gives the Mint codename while you need the Ubuntu one - e.g. you need `focal` not `una`. Using add-apt-repository will avoid that issue - but unsually it will not automaticall pull the authentication key. The key can be added with the Software Sources app maintenance page or with apt-key add:

##### Terminal commands - *do not execute everything blindly*
```bash
# Repository
sudo add-apt-repository https://packages.adoptium.net/artifactory/deb
# Signing key
wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | sudo apt-key add -
# Install
sudo apt update
sudo apt install temurin-17-jdk
sudo apt purge default-jre openjdk-11-* openjdk-14-*
# Check
sudo update-java-alternatives -l
java -version
```

### git and SSH
If you can't clone your fork of the repo due to login/authentication errors, consider setting up your github account for SSH access as [described here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) and summarized in the shell code section below. For example, if your account has been set up to use SSH and you move to a different machine, you could get problems - in my case there were no keys whatsoever, and therefore none that matched those github knew about.

If you generate a key, you'll want to decide whether it can be reused (just use or generate a default one) or it's meant to be specific for github development, and whether to use an empty passphrase or maximize security - beware that you'll need to actually type it at least once; as pasting a keepass-generated password won't work in all places, the `ssh-add` command blocks the clipboard by design. You will also need that passphrase at least once while cloning your repo in Android Studio. You will also have to decide on a filename and the "comment" field - I'd suggest using the actual github account name for the former and the actual email the account is registered to for the latter. I suspect, however, that neither match is strictly necessary.

##### Terminal commands - *do not execute everything blindly*
```bash
# Check which SSH keys exist (uppercase L!):
ssh-add -L
# If there's a listing and any of these seem suitable, copy the whole line into the clipboard and use it to register the key at github - see below.
# Generate a new key, decide on and replace <filename> (suggested: your github name), <comment> (suggested: your github email) and <passphrase> (your choice) as needed:
cd ~/.ssh
ssh-keygen -t ed25519 -C "<comment>" -f <filename> -N "<passphrase>"
# Just make sure the ssh agent is running - output irrelevant unless some scary errors
eval "$(ssh-agent -s)"
# Add the key, type your passphrase, do not copy&paste it
ssh-add ./<filename>
# List keys
ssh-add -L
# copy the whole line corresponding to your new key, and in your browser go to yout github profile settings, "SSH and GPG keys" section, add new and paste that line. Done!
```

### Push email and privacy
Sooner or later you'll want to push, and at that point git wants an email address. This is used for authorship and independent from account login. If your github account is new and in a default state, you could get away with providing the one you used to create that account and it would work. If, however, you might consider keeping that mail private, or have done so in the past, you'll need a little more preparation.

* In your browser, go to your github account's [settings, section emails](https://github.com/settings/emails#toggle_visibility). If the option "Keep my email addresses private" is checked (and I *would* recommend you set it), none of the emails listed above that are useable for said push mail setting. The one listed in small bold font right under the option is the right one - copy & paste that once the first push asks.
* If you've already stepped into the trap, getting the "push declined due to email privacy restrictions" error, you'll need to fix that from the command line. This works without needing to close the IDE or your project. Look for the commands below, but take that github proxy mail as described above and replace one or two placeholders with it.

##### Terminal commands - *do not execute everything blindly*
```bash
# Fix 'push declined due to email privacy' - take that proxy mail from your github account settings:
git config --global user.email "xxxx+youraccount@users.noreply.github.com"
cd <your-project's-root-folder>
# Force re-association
git commit --amend --reset-author
# Show project-local mail setting
git config user.email
# Check the output - if empty or equal to the one used above, fine. If it's the private one, overwrite as follows (note no --global):
git config user.email "xxxx+youraccount@users.noreply.github.com"
# retry your push - should pass
```

### Markdown
It might be useful to have markdown support as some documents a contributor might want to edit are Markdown, e.g. source attribution for imported open media resources.

There's an IntelliJ [plugin for Markdown fom JetBrains](https://plugins.jetbrains.com/plugin/7793-markdown) that can be installed directly from the Settings Plugins page.

A nice Markdown cheat sheet is [here](https://www.markdownguide.org/cheat-sheet) - though only 90% applies to files that will be rendered by github. Particularly, footnotes work differently.

From time to time it can be useful to post large blocks of (code, savegames) without creating posts several pages long - this can be done with a 'spoiler' technique which unfortunately on github requires embedding html directly ([reference](https://stackoverflow.com/questions/32814161/how-to-make-spoiler-text-in-github-wiki-pages)):
```html
<details>
  <summary>Visible clickable header not using markdown but html formatting</summary>

Markdown - leave empty lines before/after

</details>
```
Would look like this:
<details>
  <summary>Visible header not using markdown but html formatting</summary>

Markdown - leave empty lines before/after

</details>

On footnotes - if you really need those you'd have to fake it using inline html like so:
```html
    Footnote reference in main body: <sup id="a1">[name](#f1)</sup>

    Footnote definition below: <sup id="f1">name</sup> ...footnote text... [↩](#a1)
```
Just make sure to match up the id's (`a1`, `f1`) if you define several footnotes. Using `sup` to format both reference and definition marker is optional, `b` `i` or `span` work just as well.

### Avoid pushing private changes, texture updates
You _don't_ want to include your testing data - mods, saved games, settings, etc. in your pushes. `.gitignore` helps with that, but Android Studio interprets that loosely, meaning clicking a wrong checkbox can include such files anyway.

Also, changes to `.gitignore` itself would normally be part of a commit - but `.git/info/exclude` would not. Therefore - use the former only if you want the change to affect the whole team, and wrap the change in its own PR and explain why the exclusion is good for all. All other ignores should go to `.git/info/exclude`.

Another factor: git branch checkouts will update file timestamps, so an Unciv run might decide to re-pack textures and build new atlas files, even if you didn't actually add graphics. Care shoud be taken only actual content affecting atlas / texture png changes are pushed. Inversely, you need to take care that texture packs _are_ run when needed and the result included in pushes - if the folder structure changes, or you copy or move files without them getting fresh timestamps. In such cases, delete the atlas file to force a re-pack and run Unciv once.

### Initial Run Config
Setting up the desktop run config depends a bit on the IDE knowing about the project contents, so it's best to wait a little after cloning until the initial automatic gradle *sync* has finished, which can take a quarter of an hour. Otherwise the dropdown for "use classpath" will not contain the desktop entry.

The existing [Getting-Started](https://github.com/yairm210/Unciv/wiki/Getting-Started) says to "set <repo_folder>\android\assets\ as the Working directory", but I prefer a slight modification, see above.

*Outside* the folder which the IDE sees as the mirror of your fork, say that is `~/Development/foo/bar/Unciv`, create a parallel one for use as Working directory, which might be `~/Development/foo/bar/Unciv.workdir`, and set that in your desktop run config. Then link some subfolders from the mentioned assets folder and copy the textures as follows:
```bash
# cd to your new empty working folder (or use the open in terminal feature of your file manager)
ln -s ../Unciv/android/assets/ExtraImages
ln -s ../Unciv/android/assets/jsons
ln -s ../Unciv/android/assets/sounds
cp ../Unciv/android/assets/*.atlas .
cp ../Unciv/android/assets/*.png .
```
(This is not necessarily complete - I also set up links for Image folders and other stuff - this is a _guideline_ only)
This means data added due to playtesting ***cannot*** affect commits and you can test with mods without them appearing in Android Studio, no need to fiddle with exlusions and making sure the exclusion list does not end up in a commit - except if you use the "generate translation files" button. Caveat: If your proposed change actually needs to change the atlas/texture files that should be part of a release, you'll _have_ to copy them back manually.
