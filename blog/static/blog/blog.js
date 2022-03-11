function edit(elem) {
    var element = elem
    console.log(element)
    above = element.previousElementSibling
    nextabove = above.previousElementSibling

    var content = nextabove.innerHTML
    var id = nextabove.id

    const textarea = document.createElement("textarea");
    textarea.setAttribute("id", "jstextarea");

    const jsbutton = document.createElement("button");
    jsbutton.innerHTML = "Submit Edit!";
    jsbutton.setAttribute("id", "jseditbutton");
    jsbutton.setAttribute("class", "btn btn-danger");
    
    //parent = element.parentNode;
    //console.log(parent)
    //var text = parent.querySelector('p');
    
    textarea.innerHTML = content

    nextabove.replaceWith(textarea);
    element.replaceWith(jsbutton);

    btn = document.querySelector('#jseditbutton');
    ta = document.querySelector('#jstextarea');

    btn.addEventListener('click', () => 


    fetch(`/blog/articles/5`, {
        method: 'PUT',
        headers: {'X-CSRFToken': csrftoken},
        body: JSON.stringify({
            id: id,
            content: ta.value,
        }),
        mode : 'same-origin' // For same origin requests 
    })
    .then(response => response.text())
    .then(response => {
        jsbutton.replaceWith(elem)
        nextabove.innerHTML = ta.value 
        textarea.replaceWith(nextabove) 
    }));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');