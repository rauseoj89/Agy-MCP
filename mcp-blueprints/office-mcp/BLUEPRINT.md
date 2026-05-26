# Office-MCP Blueprint 📁 *(In Progress)*

`office-mcp` is a secure, automated document builder designed to read and generate word processing sheets, slides, spreadsheet files, and portable document formats (PDFs).

## 📁 Structure

* **`BLUEPRINT.md`**: This manual.
* **`schemas/`**: JSON tool definition files.
* **`templates/`**: Word, Excel, and PPT boilerplate structures.

## 🚀 Capabilities

1. **Read Office File (`read_office_file`)**: Loads and extracts text or cell blocks from `.docx`, `.xlsx`, and `.pdf` files.
2. **Write Word Document (`write_word_document`)**: Dynamically writes structures, styles, and text blocks to a `.docx` file.
3. **Write Excel Sheet (`write_excel_sheet`)**: Exports structured arrays, matrix grids, and math models into `.xlsx` documents.
4. **Write PDF Document (`write_pdf_document`)**: Renders system audit files, reports, or invoices into standard `.pdf` outputs.
5. **Write PowerPoint Presentation (`write_powerpoint_presentation`)**: Auto-builds slides, headers, and media blocks into a `.pptx` slide deck.

---

## 🛠️ Status & Development Notes
* This MCP is located in `P:\Workspaces\Development\Efficiency-Core\mcp\office-mcp`.
* Main files: `readers.ts` handles reading engines, `writers.ts` drives file compilers, and `legacy_reader.py` processes older binaries.
