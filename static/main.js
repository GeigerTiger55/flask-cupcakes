"use strict";

const $allCupcakesList = $("#all-cupcakes-list");

const $submitForm = $("#add-cupcake-form");

/** Overall function to kick off the app. */

async function start() {
    console.debug("start");
    console.log('cupcakes list in start', $allCupcakesList)
    await getAndShowCupcakesOnStart();

}

$(start);