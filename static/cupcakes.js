"use strict";

// This is the global list of the cupcakes, an instance of CupcakeList
let cupcakeList;

async function getAndShowCupcakesOnStart() {
    console.debug("getAndShowCupcakeOnStart")
    cupcakeList = await CupcakeList.getCupcakes();

    putCupcakesOnPage();
}


/**
 * A render method to render HTML for an individual cupcake instance
 * - cupcake: an instance of Cupcake
 *
 * Returns the markup for the cupcake.
 */
function generateCupcakeMarkup(cupcake) {
    console.debug("generateCupcakeMarkup")
    return $(`
      <li id="${cupcake.id}">
        <img src="${cupcake.image}" width="250"> 
        Flavor: ${cupcake.flavor}, Size: ${cupcake.size}, Rating: ${cupcake.rating}
      </li>
    `);
}


/** Gets list of cupcakes from server, generates their HTML, and puts on page. */

function putCupcakesOnPage() {
  console.debug("putCupcakesOnPage");
  $allCupcakesList.empty();
  console.debug('cupcake list', cupcakeList.cupcakes);
  // loop through all of our cupcakes and generate HTML for them
  for (let cupcake of cupcakeList.cupcakes) {
      const $cupcake = generateCupcakeMarkup(cupcake);
      console.log('cupcake obj', $cupcake);
      $allCupcakesList.append($cupcake);
  }

  //$allCupcakesList.show();
}


/**When user submits the form, add cupcake to database and to the cupcake
 *  list */
async function getInputsAndAddCupcake(evt) {
  console.debug("getInputsAndAddCupcake");
  evt.preventDefault();
    const flavor = $("#flavor").val();
    const size = $("#size").val();
    const rating = $("#rating").val();
    const imgUrl = $("#image").val();
    
    const cupcakeInfo = {
      flavor,
      size,
      rating,
      imgUrl,
    };

    const newCupcake = await cupcakeList.addCupcake(cupcakeInfo);
    addNewCupcakeOnPage(newCupcake);

    //Clear form and hide
    $submitForm.trigger("reset");
}

$submitForm.on("submit", getInputsAndAddCupcake);

/**Add new cupcake to page */
function addNewCupcakeOnPage(newCupcake) {
  console.debug("addNewCupcakeOnPage");
  const cupcakeHTML = generateCupcakeMarkup(newCupcake);
  $allCupcakesList.prepend(cupcakeHTML);
}