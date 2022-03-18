onResize = function() {
    var db = document.body;
    var sx = db.clientWidth / window.innerWidth;
    var sy = db.clientHeight / window.innerHeight;
    var transform = "scale(" + (1 / Math.max(sx, sy)) + ")";

    db.style.MozTransform = transform;
    db.style.WebkitTransform = transform;
    db.style.OTransform = transform;
    db.style.msTransform = transform;
    db.style.transform = transform;
}

handleMulticolumns = function() {

    var elements = document.getElementsByClassName('multicol');
    var elem, parent, sybling;
    var i, j;
    var nCols;

    for (i = 0; i < elements.length; i++) {

        elem = elements[i];
        nCols = parseInt(elem.getAttribute('cols'));

        parent = elem.parentElement;
        parent.setAttribute('colspan', nCols);

        elem = parent;
        parent = elem.parentElement;

        for (j = 1; j < nCols; j++) {

            sybling = elem.nextElementSibling;
            parent.removeChild(sybling);
        }
    }
}

handleMultirows = function() {

    var elements = document.getElementsByClassName('multirow');
    var elem, parent, uncle;
    var i, j, k;
    var nRows;
    var elementCellIndex;

    for (i = 0; i < elements.length; i++) {

        elem = elements[i];
        nRows = parseInt(elem.getAttribute('rows'));

        parent = elem.parentElement;
        parent.setAttribute('rowspan', nRows);

        elem = parent;
        parent = elem.parentElement;
        uncle = parent;

        elementCellIndex = elem.cellIndex;
        for (j = 1; j < nRows; j++) {

            uncle = uncle.nextElementSibling;
            uncle.removeChild(uncle.children[elementCellIndex]);
        }
    }
}

window.onresize = onResize;
document.addEventListener("DOMContentLoaded", onResize);
document.addEventListener("DOMContentLoaded", handleMulticolumns);
document.addEventListener("DOMContentLoaded", handleMultirows);

/*
 * Overload some slidy functions to change the default behavior.
 */
w3c_slidy.add_toolbar = function() {

    // Lembrar de setar: w3c_slidy.slide_number_element
    var db = document.body;
    var toolbarDiv = document.createElement("div");
    var authorNameDiv = document.createElement("div");
    var presentationNameDiv = document.createElement("div");
    var slideNumberDiv = document.createElement("div");

    toolbarDiv.className = "toolbar";
    authorNameDiv.className = "authorName";
    presentationNameDiv.className = "presentationName";
    slideNumberDiv.className = "currentSlide";

    const metas = document.getElementsByTagName('meta');
    for (let i = 0; i < metas.length; i++) {

        if (metas[i].getAttribute('name') === "author") {

            authorNameDiv.innerHTML = metas[i].getAttribute('content');
            break ;
        }
    }
    presentationNameDiv.innerHTML = document.title;
    slideNumberDiv.innerHTML = "1/1";

    toolbarDiv.style.visibility = 'hidden';

    db.appendChild(toolbarDiv);
    toolbarDiv.appendChild(authorNameDiv);
    toolbarDiv.appendChild(presentationNameDiv);
    toolbarDiv.appendChild(slideNumberDiv);

    w3c_slidy.toolbar = toolbarDiv;
    w3c_slidy.slide_number_element = slideNumberDiv;
}

w3c_slidy.show_slide_number = function() {

    w3c_slidy.slide_number_element.innerHTML = (w3c_slidy.slide_number + 1) + "/" + w3c_slidy.slides.length;
}

w3c_slidy.show_slide = function (slide) {

    this.sync_background(slide);
    this.remove_class(slide, "hidden");

    // work around IE9 object rendering bug
    setTimeout("window.scrollTo(0,0);", 1);

    if (w3c_slidy.slide_number == 0) {

        // Suppress the toolbar for the title page.
        w3c_slidy.toolbar.style.visibility = 'hidden';
    }
    else {

        // Show the toolbar for the others.
        w3c_slidy.toolbar.style.visibility = 'unset';
    }
}

w3c_slidy.add_initial_prompt = function() {}
