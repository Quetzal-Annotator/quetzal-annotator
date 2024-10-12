# quetzal-annotator
*Intro...*

# Using the Web Interface
The public web interface for *Quetzal* can be accessed at https://proteomecentral.proteomexchange.org/quetzal/

The page is divided into four main sections (_Import_, _Edit_, _Explore_, _Export_) and one for viewing debug information.

## Import
This is where a spectrum is entered into *Quetzal*.  Data can be fetched via a [Universal Spectrum Identifier](https://www.psidev.info/usi) (**USI**), or entered as a **peak list**.

A **USI** is not required to have an interpretation; in this case only basic annotation will be performed by *Quetzal*. The user can also specify which of the *PROXI* repositories to fetch spectrum data from, including private password-protected data in *PRIDE*.  For the latter, you will be prompted for your credentials, which will be used until the *Log Out* button is pressed, or the browser tab is closed.
>[!TIP]
>Not all datasets are hosted by all providers, and even portions of a given dataset may be missing for a given provider.
>Also, some providers furnish different levels of metadata.

A **peak list** consists of rows with at least two columns (*m/z* and *intensity*), with an optional third column containing peak annotations.  Columns can be separated by one or more space characters (including combinations, e.g. tabs and spaces), and empty values are not allowed. The list can either be typed/pasted into the text box, or a file of the proper format can be dragged and dropped into the same box.
Other than peaks (and optional annotations), *Quetzal* also recognizes the following special keywords when importing via the peak list mechanism: `PRECURSORMZ`, `PEPTIDOFORMS`, and `CHARGES`.  If any of these strings are present as the first column in a given line of text, the value is taken from the second column.
>[!TIP]
>When using the *Download TSV* function, the file generated contains these values (and annotations), and is thus readily importable back into *Quetzal*

Once the **USI** or **peak list** has been entered, click on the corresponding button to import the data and run the annotator. If successful, the page will switch to the _Explore_ section.

### Import via direct link
External applications may link to *Quetzal* with the optional `usi` and `provider` URL parameters. If `usi` is detected, the data will be fetched (from `provider`, if specified) and automatically annotated.

## Edit
Once a spectrum has been loaded into _Quetzal_, this section allows the user to add or modify spectrum properties such as precursor m/z and charge, as well as the peptidoform. Editing the latter can be useful when testing alternate interpretations of a particular spectrum, and must follow the [PSI ProForma notation](https://github.com/HUPO-PSI/ProForma).  The annotator parameters of fragmentation type and m/z tolerance for matching ions can also be set here.
>[!TIP]
>HCD and CID consider only _a/b/y_ backbone ions, ETD considers only _c/z_, while EThcD considers them all.

The lower pane displays the current annotations, and allows the user to edit them individually.  While _Quetzal_ follows the [PSI mzPAF](https://github.com/HUPO-PSI/mzPAF) format, the user is free to type any text (or none) when annotating peaks.

## Explore
View annotated spectrum with zoom interaction.  Also matched ion table, stats, and full annotated peak list...

## Export
Export publication-quality scalable figures, with various controls and preview mode...

## Log / Errors
View detailed messages; useful for debugging or reporting issues to the dev team...
