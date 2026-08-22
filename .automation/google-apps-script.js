// ===== COPY THIS ENTIRE CODE TO Google Apps Script =====
// Steps:
// 1. Go to script.google.com
// 2. Open your project (or create new)
// 3. Delete all existing code
// 4. Paste this ENTIRE code
// 5. Replace SHEET_ID with your Google Sheet ID
// 6. Save (Ctrl+S)
// 7. Deploy → New Deployment → Web App → Execute as: Me → Anyone → Deploy
// 8. Copy the new Web App URL

var SHEET_ID = 'REPLACE_WITH_YOUR_GOOGLE_SHEET_ID';

// This function handles POST requests (form submissions)
function doPost(e) {
  try {
    var sheet = SpreadsheetApp.openById(SHEET_ID).getActiveSheet();

    // Add headers if sheet is empty
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Timestamp', 'Name', 'Phone', 'Email', 'Interest', 'Page', 'Status']);
    }

    // Get form data
    var data = e.parameter;

    // Add row to sheet
    sheet.appendRow([
      new Date(),
      data.name || '',
      data.phone || '',
      data.email || '',
      data.interest || '',
      data.page || '',
      'New'
    ]);

    // Return success response
    return ContentService.createTextOutput(JSON.stringify({
      status: 'success',
      message: 'Lead saved successfully'
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: 'error',
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

// This function handles GET requests (browser visits)
function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({
    status: 'ok',
    message: 'Sainik School Guide - Lead Form Endpoint Active',
    timestamp: new Date().toString()
  })).setMimeType(ContentService.MimeType.JSON);
}
