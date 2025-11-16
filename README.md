# mddr-ipspatchgen
An IPS patch generator for MDDR.<br>
## Structure
The structure of a MDDR IPS patch is pretty easy to understand.
### Header
The header starts with the word "PATCH".<br>
<img src="./assets/patchheader.png" alt="Example of Patch Header"/><br>
Then, the Patch Name follows the word, and ends with 0x00 as an EOF.<br>
<img src="./assets/patchname.png" alt="Example of Patch Name"/><br>