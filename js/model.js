M = {
  defaultRuleString: (30).toString(2),

  setRule: function (ruleString) {
    var prefix = Array(8 - ruleString.length).fill(0).join('')
    ruleString = prefix + ruleString
    this.rule = {
      '111': ruleString[0] | 0,
      '110': ruleString[1] | 0,
      '101': ruleString[2] | 0,
      '100': ruleString[3] | 0,
      '011': ruleString[4] | 0,
      '010': ruleString[5] | 0,
      '001': ruleString[6] | 0,
      '000': ruleString[7] | 0
    }
  },

  getNewState: function () {
    if (!this.state) {
      this.state = this.getInititalState()
      controls.drawInitState(this.state)
    } else {
      this.state = this.calculateState(this.state)
    }

    return this.state
  },

  getInititalState: function () {
    var state = Array(this.size)
    switch (this.stateType) {
      case 'one':
        state.fill(0)
        state[parseInt(state.length / 2)] = 1
        return state
      case 'random':
      default:
        return this.getRandomInitialState()
    }
  },

  getRandomInitialState: function () {
    var state = Array(this.size)
    for (var i = 0; i < state.length; i++) {
      state[i] = Math.round(Math.random()); // {0, 1}
    }
    return state
  },

  calculateState: function (previousState) {
    var newState = Array(previousState.length)

    for (var i = 0; i < previousState.length; i++) {
      newState[i] = this.getCellValue(
        i === 0 ? previousState[previousState.length - 1] : previousState[i - 1] | 0,
        previousState[i],
        i === previousState.length - 1 ? previousState[0] : previousState[i + 1] | 0
      )
    }

    return newState
  },

  getCellValue: function (left, current, right) {
    if (!this.rule) {
      this.setRule(this.defaultRuleString)
    }

    var key = [left, current, right].join('')
    return this.rule[key]
  },

  skr: function (firstNumbers, secondNumbers, splitNumber) {
      var a = firstNumbers.slice(0, splitNumber),
          b = firstNumbers.slice(splitNumber),
          c = secondNumbers.splice(0, splitNumber),
          d = secondNumbers.splice(splitNumber);

      return [
          [].concat(a, d),
          [].concat(b, c)
      ]
  },

  mute: function () {},

  doTests: function () {}
}
