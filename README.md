# Python script to generate an HTML email signature

1. Fork this repository
2. Clone this repository to your local machine
3. Generate a custom HTML email signature by running the following command in the terminal:
```bash
$ ./generate-email-signature.py
```
This will generate a file with format `<Name>.html`
4. Open your signature in the browser by running the following command in the terminal:
```bash
browse <Name>.html
```
Note: The signature will look squashed with the text overlapping, but Gmail add additional line spacing that will correct this.
5. Add your custom `<Name>.html` signature to your email as follows:
- Go to `Settings`, then `General`
- Scroll down to the `Signature:` section
- Select `+ Create new`
- Go back to the HTML file in your browser (from step 4) and highlight the entire signature
- Drag and drop the signature into the signature box
- Use the drop-down options to choose when your email signature should be included
- Scroll down and click `Save Changes`


