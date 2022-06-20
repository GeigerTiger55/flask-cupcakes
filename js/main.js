"use strict";

const $allCupcakesList = $("#all-cupcakes-list")

/** Overall function to kick off the app. */

async function start() {
    console.debug("start");

    await getAndShowCupcakesOnStart();

}

$(start);