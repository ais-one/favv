// improved download function
function downloadData(content, filename, type = 'text/csv;charset=utf-8;') {
  const blob = new Blob([content], { type })
  // IE11 & Edge
  if (navigator.msSaveBlob) {
    // IE hack; see http://msdn.microsoft.com/en-us/library/ie/hh779016.aspx
    navigator.msSaveBlob(blob, filename)
  } else {
    // In FF link must be added to DOM to be clicked
    const link = document.createElement('a')
    link.href = window.URL.createObjectURL(blob)
    link.setAttribute('download', filename)
    document.body.appendChild(link)
    link.click() // IE: "Access is denied"; see: https://connect.microsoft.com/IE/feedback/details/797361/ie-10-treats-blob-url-as-cross-origin-and-denies-access
    document.body.removeChild(link)
  }
}

// https://stackoverflow.com/questions/8847766/how-to-convert-json-to-csv-format-and-store-in-a-variable
function jsonToCsv (items) {
  const replacer = (key, value) => value === null ? '' : value // specify how you want to handle null values here
  const header = Object.keys(items[0])
  const csv = [
    header.join(','), // header row first
    ...items.map(row => header.map(fieldName => JSON.stringify(row[fieldName], replacer)).join(','))
  ].join('\r\n')
  // var fields = Object.keys(json[0])
  // var replacer = function(key, value) { return value === null ? '' : value } 
  // var csv = json.map(function(row){
  //   return fields.map(function(fieldName){
  //     return JSON.stringify(row[fieldName], replacer)
  //   }).join(',')
  // })
  // csv.unshift(fields.join(',')) // add header column
  // csv = csv.join('\r\n')
  return csv
}

export { downloadData, jsonToCsv }
