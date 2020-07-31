import React from "react";
import ReactDOM from "react-dom";
import { Fragment } from "react-is";
class App extends React.Component {
  render() {
    return (
      <Fragment>
        <a
          className="uk-navbar-toggle tm-navbar-button"
          href="#"
          data-uk-search-icon
        ></a>
        <div
          className="uk-navbar-dropdown uk-padding-small uk-margin-remove"
          data-uk-drop="mode: click;cls-drop: uk-navbar-dropdown;boundary: .tm-navbar-container;boundary-align: true;pos: bottom-justify;flip: x"
        >
          <div className="uk-container">
            <div className="uk-grid-small uk-flex-middle" data-uk-grid>
              <div className="uk-width-expand">
                <form className="uk-search uk-search-navbar uk-width-1-1">
                  <input
                    className="uk-search-input"
                    type="search"
                    placeholder="Search…"
                    autoFocus
                  />
                </form>
              </div>
              <div className="uk-width-auto">
                <a
                  className="uk-navbar-dropdown-close"
                  href="#"
                  data-uk-close
                ></a>
              </div>
            </div>
          </div>
        </div>
        <a
          className="uk-navbar-item uk-link-muted uk-visible@m tm-navbar-button"
          href="compare.html"
        >
          <span data-uk-icon="copy"></span>
          <span className="uk-badge">3</span>
        </a>
        <a
          className="uk-navbar-item uk-link-muted tm-navbar-button"
          href="account.html"
          data-uk-icon="user"
        ></a>
        <div
          className="uk-padding-small uk-margin-remove"
          data-uk-dropdown="pos: bottom-right; offset: -10; delay-hide: 200;"
          style={{ minWidth: "150px" }}
        >
          <ul className="uk-nav data-uk-dropdown-nav">
            <li>
              <a href="#">
                Orders
                <span>(2)</span>
              </a>
            </li>
            <li>
              <a href="#">
                Favorites
                <span>(3)</span>
              </a>
            </li>
            <li>
              <a href="#">Personal</a>
            </li>
            <li>
              <a href="#">Settings</a>
            </li>
            <li className="uk-nav-divider"></li>
            <li>
              <a href="#">Log out</a>
            </li>
          </ul>
        </div>
        <a
          className="uk-navbar-item uk-link-muted tm-navbar-button"
          href="cart.html"
          data-uk-toggle="target: #cart-offcanvas"
          // onClick="return false"
        >
          <span data-uk-icon="cart"></span>
          <span className="uk-badge">2</span>
        </a>
      </Fragment>
    );
  }
}
ReactDOM.render(<App />, document.getElementById("navbar-content"));
