import fitz  # PyMuPDF

doc = fitz.open("input.pdf")

for page in doc:
    areas = page.search_for("API testing with Postman")
    for inst in areas:
        page.add_redact_annot(inst, fill=(1, 1, 1))
    page.apply_redactions()
    for inst in areas:
        # Insert new text at top-left of old text area
        page.insert_text(
            (inst.x0, inst.y0 + 8.5),  # shift 2px up
            "API testing with REST assured.",
            fontsize=10,
            fontname="Times-Roman",
            color=(0, 0, 0)
        )

doc.save("output.pdf")
print("done")