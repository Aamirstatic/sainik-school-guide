// Google Apps Script - Copy this to script.google.com
// Steps:
// 1. Go to script.google.com
// 2. Create new project
// 3. Paste this code
// 4. Create a Google Sheet
// 5. Replace SHEET_ID below with your Google Sheet ID
// 6. Deploy as Web App (Execute as: Me, Access: Anyone)
// 7. Copy the Web App URL
// 8. Replace the URL in lead-form.html

var SHEET_ID = 'REPLACE_WITH_YOUR_GOOGLE_SHEET_ID';

function doPost(e) {
  var sheet = SpreadsheetApp.openById(SHEET_ID).getActiveSheet();

  // Add headers if first row
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Timestamp', 'Name', 'Phone', 'Email', 'Interest', 'Page', 'Status']);
  }

  var data = e.parameter;
  sheet.appendRow([
    new Date(),
    data.name || '',
    data.phone || '',
    data.email || '',
    data.interest || '',
    data.page || '',
    'New'
  ]);

  return ContentService.createTextOutput(JSON.stringify({ status: 'success' }))
    .setMimeType(ContentService.MimeType.JSON);
}

function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({ status: 'ok', message: 'Lead form endpoint active' }))
    .setMimeType(ContentService.MimeType.JSON);
}
