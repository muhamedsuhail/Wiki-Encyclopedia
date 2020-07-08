
document.addEventListener('DOMContentLoaded',()=>{
    
    // If userAgent is a Mobile/Tab trigger touchstart events.
    
    var click_event=(/iPhone|iPad|iPod|Android/i.test(navigator.userAgent))? 'touchstart':'click';
    
    // CodeMirror library for configuring Textarea as Code Editor.
    
    var editor=CodeMirror.fromTextArea(document.querySelector('textarea'),{
        
        lineNumbers: true,
        mode:"markdown",
        highlightFormatting: true,
        theme:"dracula",
        placeholder:"# Enter the Content of the new entry in Markdown."

    });

    // Populates the title and editor with existing Markdown content of the page. (For Editing Entry)
    
    var title=document.querySelector('title').text
    document.querySelector('#new_entry').querySelector('form').title.value=(title!="New Entry")? title:"";
    
    if(title=="New Entry")
    {
        editor.setValue("");
    }
    else if(cont)
    {
        editor.setValue(cont);
    }

    // Change size of the editor with respect to the device.
    
    if(click_event=='touchstart')
    {
        editor.setSize("90vw","70vh");
    }
    else{
        editor.setSize("80vw","70vh");
    }
})
