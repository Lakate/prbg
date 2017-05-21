V = {
    BG_COLOR: [255,255,255,255],
    FILL_COLOR: [0,0,0,255],
    hexToRGBA: function(hex) {
      var r = parseInt(hex.slice(0,2), 16),
          g = parseInt(hex.slice(2,4), 16),
          b = parseInt(hex.slice(4,6), 16);
      return [r,g,b,255];
    },
    drawLine: function (lineNumber, state) {
        if (!this.ctx) {
            var canvas = this.canvas = document.getElementById("canvas");
            canvas.width = M.size;
            canvas.height = C.steps;
            var ctx = this.ctx = canvas.getContext("2d");
            ctx.moveTo(0,0);
        }
        var imageData = this.ctx.getImageData(0, lineNumber, this.canvas.width, 1);

        function drawPixel (x, r, g, b, a) {
            var index = x * 4;

            imageData.data[index] = r;
            imageData.data[index + 1] = g;
            imageData.data[index + 2] = b;
            imageData.data[index + 3] = a;
        }

        for(var i = 0; i < state.length; i++) {
            if (state[i]) {
                drawPixel.apply(null, [i].concat(this.FILL_COLOR));
            } else {
                drawPixel.apply(null, [i].concat(this.BG_COLOR));
            }
        }

        this.ctx.putImageData(imageData, 0, lineNumber);
    },

    setColors: function(bgColor, fillColor) {
        this.BG_COLOR = this.hexToRGBA(bgColor);
        this.FILL_COLOR = this.hexToRGBA(fillColor);
    }
};
