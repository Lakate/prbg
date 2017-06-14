C = {
    init: function () {
        M.size = 1000;
        this.steps = 50;
        controls.init(M.defaultRuleString);
        this.start();
    },

    start: function() {
        document.body.className = 'loading';
        setTimeout(this.draw.bind(this), 1);
    },

    draw: function() {
        var t0 = performance.now();
        M.state = null;
        for (var i = 0; i < this.steps; i++) {
            var state = M.getNewState();
            // V.drawLine(i, state);
            V.drawPopulation(state);
        }
        document.body.className = '';
    },

    setDecimalRule: function(decRule) {
        M.setRule(parseInt(decRule, 10).toString(2));
    },

    setBinaryRule: function(binRule) {
        M.setRule(parseInt(binRule, 2).toString(2));
    }
};
