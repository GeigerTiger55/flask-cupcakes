"use strict";

// This is the global list of the cupcakes, an instance of CupcakeList
let cupcakeList;

async function getAndShowCupcakesOnStart() {
    console.debug("getAndShowCupcakeOnStart")
    cupcakeList = await CupcakeList.getCupcakes();

    putCupcakesOnPage();
}

/** Gets list of cupcakes from server, generates their HTML, and puts on page. */

function putCupcakesOnPage() {
    console.debug("putCupcakesOnPage");
    $allCupcakesList.empty();

    // loop through all of our cupcakes and generate HTML for them
    for (let cupcake of cupcakeList.cupcakes) {
        const $cupcake = generateCupcakeMarkup(cupcake);
        $allCupcakesList.append($cupcake);
    }

    $allCupcakesList.show();
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
      <li id="${cupcake.cupcakeId}">
        <img src="${cupcake.image}">
        ${cupcake.flavor}, ${cupcake.size}, ${cupcake.rating}
        

      </li>
    `);
}