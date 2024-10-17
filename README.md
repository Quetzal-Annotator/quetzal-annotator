# quetzal-annotator
Quetzal is a peptide fragment ion spectrum annotation tool to assist researchers in annotating and examining tandem mass spectra to ensure that they correctly support study conclusions. Quetzal annotates spectra using the new Human Proteome Organization ([HUPO](https://hupo.org/)) Proteomics Standards Initiative ([PSI](https://psidev.info/)) [mzPAF](https://psidev.info/mzPAF/) standard for fragment ion peak annotation. Quetzal includes a Python-based codebase, a web-service endpoint that provides annotation services, and a user-friendly web-based application for annotating spectra and producing publication-quality figures. 

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
This section features an interactive annotated spectrum, along with a matched ion table, basic ion statistics, and full annotated peak list.

The top left corner of the **MS/MS spectrum** shows the experimental _m/z_, the calculated _peptidoform m/z_, and the difference in parts per million (ppm).  The spectrum can be zoomed in to potentially reveal smaller peaks and extra annotations that are otherwise hidden to avoid overcrowding the display.  The _Reset Zoom_ button reverts the view to the original (full) scale.

The **matched ion series table** highlights those positions where an ion has been detected; bright colors indicate detection of the main (backbone) ion, whereas a darker shade indicates detection only via a neutral loss (e.g. H2O loss from a backbone ion).  Amino acids or terminii with mass modifications are highlighted in yellow.

Below that, the **peak annotations table** provides comprehensive data on each peak in the spectrum: _m/z_; intensity, both _raw_ and _normalized_ (where 100.0 corresponds to the highest intensity peak, along with a light green shaded bar); and a highlighted _ion type_.  The ion types, in order from left to right, are: backbone **a**/**b**/**c**/**x**/**y**/**z**, **I**mmonium, **prec**ursor, isobaric **rep**orter, **int**ernal fragment, **mol**ecular formula, unknown (**?**), and those identified to a molecule **other** than the identified peptidoform.  The bottom of the table shows the share of the total intensity ascribed to each of the ion types.  This information is also available graphically by clicking on the _Ion Stats_ link at the top right of this table.  A _mass defect_ plot is also available.

>[!TIP]
>The ion annotation color scheme is preserved across the various views, so that all data associated with _e.g._ a y-ion is always shown in red.

## Export
This section enables the production of publication-quality figures, as well as text output of the annotated spectrum.

The _Preview_ button displays the image on the page just as it would be generated, and thus allows the user to test various configurations and settings before final download. There are options for downloading a Scalable Vector Graphics (**SVG**) or Portable Document Format (**PDF**) file, both of which are inherently resolution-agnostic and thus will not suffer from pixelation effects.  The former can easily be imported or included in various media, such as web pages, _Word_ documents, _PowerPoint_ slides, etc; the latter is more apt as a single-page document that may be compiled as e.g. supplementary material.

Other than the min/max m/z range and y max (where 1.0 = most intense peak), there are output options to hide/display the following elements:
![image](https://github.com/user-attachments/assets/abc579ba-17ca-4e5e-8b29-38a88662b21c)

## Log / Errors
This section contains detailed messages reported by the application, which can be useful for debugging or reporting issues.


