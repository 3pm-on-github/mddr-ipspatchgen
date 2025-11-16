# mddr-ipspatchgen
An IPS patch generator for MDDR.<br>
## Structure
The structure of a MDDR IPS patch is pretty easy to understand.
### Header
The header starts with the word "PATCH".<br>
[Patch Header](https://raw.githubusercontent.com/3pm-on-github/mddr-ipspatchgen/refs/heads/main/assets/patchheader.png)<br>
Then, the Patch Name follows the word, and ends with 0x00 as an EOF.<br>
[Patch Name](https://raw.githubusercontent.com/3pm-on-github/mddr-ipspatchgen/refs/heads/main/assets/patchname.png)<br>