"use strict";

function _instanceof(left, right) {
  if (
    right != null &&
    typeof Symbol !== "undefined" &&
    right[Symbol.hasInstance]
  ) {
    return right[Symbol.hasInstance](left);
  } else {
    return left instanceof right;
  }
}

function _typeof(obj) {
  if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") {
    _typeof = function _typeof(obj) {
      return typeof obj;
    };
  } else {
    _typeof = function _typeof(obj) {
      return obj &&
        typeof Symbol === "function" &&
        obj.constructor === Symbol &&
        obj !== Symbol.prototype
        ? "symbol"
        : typeof obj;
    };
  }
  return _typeof(obj);
}

function _classCallCheck(instance, Constructor) {
  if (!_instanceof(instance, Constructor)) {
    throw new TypeError("Cannot call a class as a function");
  }
}

function _defineProperties(target, props) {
  for (var i = 0; i < props.length; i++) {
    var descriptor = props[i];
    descriptor.enumerable = descriptor.enumerable || false;
    descriptor.configurable = true;
    if ("value" in descriptor) descriptor.writable = true;
    Object.defineProperty(target, descriptor.key, descriptor);
  }
}

function _createClass(Constructor, protoProps, staticProps) {
  if (protoProps) _defineProperties(Constructor.prototype, protoProps);
  if (staticProps) _defineProperties(Constructor, staticProps);
  return Constructor;
}

function _possibleConstructorReturn(self, call) {
  if (call && (_typeof(call) === "object" || typeof call === "function")) {
    return call;
  }
  return _assertThisInitialized(self);
}

function _getPrototypeOf(o) {
  _getPrototypeOf = Object.setPrototypeOf
    ? Object.getPrototypeOf
    : function _getPrototypeOf(o) {
        return o.__proto__ || Object.getPrototypeOf(o);
      };
  return _getPrototypeOf(o);
}

function _assertThisInitialized(self) {
  if (self === void 0) {
    throw new ReferenceError(
      "this hasn't been initialised - super() hasn't been called"
    );
  }
  return self;
}

function _inherits(subClass, superClass) {
  if (typeof superClass !== "function" && superClass !== null) {
    throw new TypeError("Super expression must either be null or a function");
  }
  subClass.prototype = Object.create(superClass && superClass.prototype, {
    constructor: { value: subClass, writable: true, configurable: true }
  });
  if (superClass) _setPrototypeOf(subClass, superClass);
}

function _setPrototypeOf(o, p) {
  _setPrototypeOf =
    Object.setPrototypeOf ||
    function _setPrototypeOf(o, p) {
      o.__proto__ = p;
      return o;
    };
  return _setPrototypeOf(o, p);
}

function _defineProperty(obj, key, value) {
  if (key in obj) {
    Object.defineProperty(obj, key, {
      value: value,
      enumerable: true,
      configurable: true,
      writable: true
    });
  } else {
    obj[key] = value;
  }
  return obj;
}

var BlogContent =
  /*#__PURE__*/
  (function (_React$Component) {
    _inherits(BlogContent, _React$Component);

    function BlogContent(props) {
      var _this;

      _classCallCheck(this, BlogContent);

      _this = _possibleConstructorReturn(
        this,
        _getPrototypeOf(BlogContent).call(this, props)
      );

      _defineProperty(_assertThisInitialized(_this), "handleShow", function () {
        if (_this.state.showResults) {
          _this.setState({
            showResults: false,
            toggleText: "Show Blog's content"
          });
        } else {
          _this.setState({
            showResults: true,
            toggleText: "Hide Blog's content"
          });
        }
      });

      _this.state = {
        showResults: false,
        toggleText: "Show Blog's content"
      };
      return _this;
    }

    _createClass(BlogContent, [
      {
        key: "render",
        value: function render() {
          return React.createElement(
            "div",
            null,
            React.createElement("input", {
              className: "btn btn-info mb-3",
              type: "submit",
              value: this.state.toggleText,
              onClick: this.handleShow
            }),
            this.state.showResults ? React.createElement(Results, null) : null
          );
        }
      }
    ]);

    return BlogContent;
  })(React.Component);

function Results() {
  var mark = document.getElementById("raw-markdown").textContent.trim();
  return React.createElement("div", {
    id: "blog-content",
    dangerouslySetInnerHTML: {
      __html: marked(mark)
    }
  });
}

ReactDOM.render(
  React.createElement(BlogContent, null),
  document.getElementById("markdown-container")
);


/* Vanila JavaScript HERE */

// Inline Markdown for Description
const descr = document.getElementById("description");
const prety_descr = marked(descr.textContent.trim());
descr.innerHTML = prety_descr.replace('<p>', '').replace('</p>', '');