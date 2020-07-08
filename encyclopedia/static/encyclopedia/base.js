
document.addEventListener('DOMContentLoaded',()=>{
    
    // If userAgent is a Mobile/Tab trigger touchstart events.
    
    var click_event=(/iPhone|iPad|iPod|Android/i.test(navigator.userAgent))? 'touchstart':'click';

    var sidebar=document.querySelector('.sidebar');
    var main=document.querySelector('.main');
    
    document.querySelector('#menu').addEventListener(click_event,()=>{
        
        sidebar.style.animationPlayState='running'
        sidebar.style.display= (sidebar.style.display=="block") ? "none":"block";
        
        // Change sidebar height on Orientation change
        
        sidebar.style.height="100vh";
        window.addEventListener('orientationchange',()=>{
            
            if (screen.orientation["type"]=="landscape-primary"|"landscape")
            {
                console.log("landscape");
                sidebar.style.height="100%";
            }
            else
            {
                console.log("portrait");
                sidebar.style.height="100vh";
            }
        
        })

        // Sidebar width increases on menu icon trigger
        
        sidebar.classList.replace("col-lg-2","col-lg-12");

    })

})