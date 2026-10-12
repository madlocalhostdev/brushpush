// The faint, askew board behind the page (the game's Backdrop): tiles of every strength, pointing every way.
(function () {
  var faces = ["#6467AE", "#7F5CB2", "#9C56A3", "#B9567F"];
  var rims = ["#47498C", "#5D408D", "#773C7F", "#8E3B5E"];
  var turns = ["0deg", "90deg", "180deg", "270deg"];
  var seed = 20261012;
  function next() { seed = (seed * 1103515245 + 12345) % 2147483648; return seed / 2147483648; }
  // `count` white chevrons pointing right, centred in a square, like the tiles in the game and the logo.
  function chevrons(count) {
    var path = "";
    var left = 50 - count * 13 + 3;
    for (var c = 0; c < count; c++) {
      var x = left + c * 26;
      path += "M" + x + " 26l20 24-20 24";
    }
    return '<svg viewBox="0 0 100 100"><path d="' + path + '" fill="none" stroke="#fff" stroke-width="13" ' +
      'stroke-linecap="round" stroke-linejoin="round"/></svg>';
  }
  var cols = 14, rows = 22;
  var board = document.createElement("div");
  board.className = "backdrop";
  board.setAttribute("aria-hidden", "true");
  board.style.setProperty("--cols", cols);
  for (var n = 0; n < cols * rows; n++) {
    var tile = document.createElement("i");
    if (next() < 0.22) {
      tile.className = "empty";
    } else {
      var strength = Math.floor(next() * 4);
      tile.style.setProperty("--face", faces[strength]);
      tile.style.setProperty("--rim", rims[strength]);
      tile.style.setProperty("--turn", turns[Math.floor(next() * 4)]);
      tile.innerHTML = chevrons(Math.max(1, strength));
    }
    board.appendChild(tile);
  }
  document.body.prepend(board);
})();
