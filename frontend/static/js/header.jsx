import React, { Fragment, useState, useEffect } from "react";
import ReactDOM from "react-dom";

function HeaderRight(props) {
  const [cart, setCart] = useState(5);

  var originalSetItem = sessionStorage.setItem;

  sessionStorage.setItem = function (key, value) {
    var event = new Event("itemInserted");
    event.value = value; // Optional..
    event.key = key; // Optional..
    document.dispatchEvent(event);
    originalSetItem.apply(this, arguments);
  };
  var sessionStorageSetHandler = function (e) {
    if (e.key === "cartNumber") {
      setCart(e.value);
    }
  };
  document.addEventListener("itemInserted", sessionStorageSetHandler, false);

  useEffect(() => {
    sessionStorage.setItem("cartNumber", cart);
  }, [cart]);

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
        <ul className="uk-nav uk-dropdown-nav">
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
        <span className="uk-badge">{cart}</span>
      </a>
    </Fragment>
  );
}

//
//
//
// Add to cart
//
//

export const AddToCart = (props) => {
  return (
    <div id="add-to-cart" className="tm-product-card-add">
      <div className="uk-text-meta tm-product-card-actions">
        <a
          className="tm-product-card-action js-add-to js-add-to-favorites tm-action-button-active js-added-to"
          title="Add to favorites"
        >
          <span uk-icon="icon: heart; ratio: .75;" className="uk-icon">
            <svg
              width="15"
              height="15"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
              data-svg="heart"
            >
              <path
                fill="none"
                stroke="#000"
                strokeWidth="1.03"
                d="M10,4 C10,4 8.1,2 5.74,2 C3.38,2 1,3.55 1,6.73 C1,8.84 2.67,10.44 2.67,10.44 L10,18 L17.33,10.44 C17.33,10.44 19,8.84 19,6.73 C19,3.55 16.62,2 14.26,2 C11.9,2 10,4 10,4 L10,4 Z"
              ></path>
            </svg>
          </span>
          <span className="tm-product-card-action-text">Add to favorites</span>
        </a>
      </div>
      <button className="uk-button uk-button-primary tm-product-card-add-button tm-shine js-add-to-cart">
        <span
          className="tm-product-card-add-button-icon uk-icon"
          uk-icon="cart"
        >
          <svg
            width="20"
            height="20"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
            data-svg="cart"
          >
            <circle cx="7.3" cy="17.3" r="1.4"></circle>
            <circle cx="13.3" cy="17.3" r="1.4"></circle>
            <polyline
              fill="none"
              stroke="#000"
              points="0 2 3.2 4 5.3 12.5 16 12.5 18 6.5 8 6.5"
            ></polyline>
          </svg>
        </span>
        <span className="tm-product-card-add-button-text">add to cart</span>
      </button>
    </div>
  );
};

ReactDOM.render(<HeaderRight />, document.getElementById("navbar-content"));
