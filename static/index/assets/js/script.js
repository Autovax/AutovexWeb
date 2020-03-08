// Code goes here

$(document).ready(function($){
  //$("#virus_info").hide();
  var tmr1 = setInterval(tmrDispVxn, 1000);
  var prgrs1 = 0;
  var processNum = 0;
  
function tmrDispVxn() {
    console.log("_dbg in tmrDispVxn");
    if (prgrs1< 100) {
      if (prgrs1 == 30 && processNum == 0) {
        $('#status').text("found corona virus 3d structure...")        
      }
      
      if (prgrs1 == 0 && processNum == 1) {
        $('#status').text("searching ncbi journals for virus human cell receptor that virus binds to...")        
      }
      
      if (prgrs1 == 10 && processNum == 1) {
        $('#status').text("found ncbi journals with virus human cell receptor that virus binds to, creating virus blocking protein...")        
      }
      
      if (prgrs1 == 20 && processNum == 1) {
        $('#status').text("displaying virus blocking protein...")   
        var iframe = $('#framevxn');
           iframe.attr('src', 'https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?mmdbid=2por&width=300&height=300&showcommand=0&mobilemenu=1&showtitle=0');
           $("#results").show();
      }
      
      if (prgrs1 == 30 && processNum == 1) {
        $('#status').text("obtaining quotes to create protein from dna synthesis companies...")   
      }
       
      if (prgrs1 == 40 && processNum == 1) {
        $('#status').text("quote 1 complete, working on quote 2...")   
        $("#quotes").show();
        $("#quote_div1").show();
      }
      
       if (prgrs1 == 50 && processNum == 1) {
        $('#status').text("quote 2 complete, working on quote 3...")   
        
        $("#quote_div2").show();
      }
      
      if (prgrs1 == 60 && processNum == 1) {
        $('#status').text("quote 3 complete, click on the checkboxes of the plasmids you want order, then press order button")   
        
        $("#quote_div3").show();
      }
      
      if (processNum == 0)  {
      prgrs1 = prgrs1 +10;
      }
      
      if (processNum == 1)  {
      prgrs1 = prgrs1 +1;
      }
      
    } else {
      if (processNum == 0) {
      $('#status').text("displaying corona virus 3d model, click on model to rotate it in 3d space")
      
      $('#virus_info').show();
      }
    clearInterval(tmr1);
    }
    
    $('#progressBar').progressbar({
                value: prgrs1
            });
}
            
    $("#btn_genvxn").click(function(e){
           console.log('btn_genvxn clicked');
           prgrs1 = 0;
           processNum = 1;
           tmr1 = setInterval(tmrDispVxn, 1000);
            
           
           
         });
            
            

      });