import React, { Component } from "react";
import ReactDOM from "react-dom";

class SubCategory extends Component {
  constructor(props) {
    super(props);

    //
    var subcategoryData = JSON.parse(
        document.getElementById("subcategoryData").textContent
    );

    //
    this.state = {
      slug: subcategoryData.slug,
      title: subcategoryData.title,
      categoryTitle: subcategoryData.category__title,
      brands: subcategoryData.brands,
      items: subcategoryData.items,
    };
  }

  render() {
    console.log(this.state);
    return (
        <main>
          <section className="uk-section uk-section-small">
            <div className="uk-container">
              <div className="uk-grid-medium uk-child-width-1-1" data-uk-grid>
                <div className="uk-text-center">
                  <ul className="uk-breadcrumb uk-flex-center uk-margin-remove">
                    <li>
                      <a href="/">Home</a>
                    </li>
                    <li>
                      <a href="/products/catalog">Catalog</a>
                    </li>
                    <li>
                      <a href="/products/catalog/categories">
                        Laptops &amp; Tablets
                      </a>
                  </li>
                  <li>
                    <span>Laptops</span>
                  </li>
                </ul>
                <h1 className="uk-margin-small-top uk-margin-remove-bottom">
                  Laptops
                </h1>
                <div className="uk-text-meta uk-margin-xsmall-top">
                  289 items
                </div>
              </div>
              <div>
                <div className="uk-grid-medium" data-uk-grid>
                  <aside
                    className="uk-width-1-4 tm-aside-column tm-filters"
                    id="filters"
                    data-uk-offcanvas="overlay: true; container: false;"
                  >
                    <div className="uk-offcanvas-bar uk-padding-remove">
                      <div className="uk-card uk-card-default uk-card-small uk-flex uk-flex-column uk-height-1-1">
                        <header className="uk-card-header uk-flex uk-flex-middle">
                          <div className="uk-grid-small uk-flex-1" data-uk-grid>
                            <div className="uk-width-expand">
                              <h3>Filters</h3>
                            </div>
                            <button
                              className="uk-offcanvas-close"
                              type="button"
                              data-uk-close
                            ></button>
                          </div>
                        </header>
                        <div
                          className="uk-margin-remove uk-flex-1 uk-overflow-auto"
                          data-uk-accordion="multiple: true; targets: &gt; .js-accordion-section"
                          style={{ flexBasis: "auto" }}
                        >
                          <section className="uk-card-body uk-open js-accordion-section">
                            <h4 className="uk-accordion-title uk-margin-remove">
                              Prices
                            </h4>
                            <div className="uk-accordion-content">
                              <div
                                className="uk-grid-small uk-child-width-1-2 uk-text-small"
                                data-uk-grid
                              >
                                <div>
                                  <div className="uk-inline">
                                    <span className="uk-form-icon uk-text-xsmall">
                                      from
                                    </span>
                                    <input
                                      className="uk-input"
                                      type="text"
                                      placeholder="$59"
                                    />
                                  </div>
                                </div>
                                <div>
                                  <div className="uk-inline">
                                    <span className="uk-form-icon uk-text-xsmall">
                                      to
                                    </span>
                                    <input
                                      className="uk-input"
                                      type="text"
                                      placeholder="$6559"
                                    />
                                  </div>
                                </div>
                              </div>
                            </div>
                          </section>
                          <section className="uk-card-body js-accordion-section uk-open">
                            <h4 className="uk-accordion-title uk-margin-remove">
                              Brands
                            </h4>
                            <div className="uk-accordion-content">
                              <ul className="uk-list tm-scrollbox">
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="brand-1"
                                    name="brand"
                                    value="1"
                                    type="checkbox"
                                  />
                                  <label htmlFor="brand-1">
                                    <span>
                                      Acer
                                      <span className="uk-text-meta uk-text-xsmall">
                                        177
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="brand-2"
                                    name="brand"
                                    value="2"
                                    type="checkbox"
                                  />
                                  <label htmlFor="brand-2">
                                    <span>
                                      Apple
                                      <span className="uk-text-meta uk-text-xsmall">
                                        18
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="brand-3"
                                    name="brand"
                                    value="3"
                                    type="checkbox"
                                  />
                                  <label htmlFor="brand-3">
                                    <span>
                                      ASUS
                                      <span className="uk-text-meta uk-text-xsmall">
                                        150
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="brand-4"
                                    name="brand"
                                    value="4"
                                    type="checkbox"
                                  />
                                  <label htmlFor="brand-4">
                                    <span>
                                      Dell
                                      <span className="uk-text-meta uk-text-xsmall">
                                        170
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="brand-5"
                                    name="brand"
                                    value="5"
                                    type="checkbox"
                                  />
                                  <label htmlFor="brand-5">
                                    <span>
                                      HP
                                      <span className="uk-text-meta uk-text-xsmall">
                                        498
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="brand-6"
                                    name="brand"
                                    value="6"
                                    type="checkbox"
                                  />
                                  <label htmlFor="brand-6">
                                    <span>
                                      MSI
                                      <span className="uk-text-meta uk-text-xsmall">
                                        54
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="brand-7"
                                    name="brand"
                                    value="7"
                                    type="checkbox"
                                  />
                                  <label htmlFor="brand-7">
                                    <span>
                                      Samsung
                                      <span className="uk-text-meta uk-text-xsmall">
                                        1
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="brand-8"
                                    name="brand"
                                    value="8"
                                    type="checkbox"
                                  />
                                  <label htmlFor="brand-8">
                                    <span>
                                      Sony
                                      <span className="uk-text-meta uk-text-xsmall">
                                        1
                                      </span>
                                    </span>
                                  </label>
                                </li>
                              </ul>
                            </div>
                          </section>
                          <section className="uk-card-body js-accordion-section uk-open">
                            <h4 className="uk-accordion-title uk-margin-remove">
                              Type
                              <span
                                className="tm-help-icon"
                                data-uk-icon="icon: question; ratio: .75;"
                                onClick="event.stopPropagation();"
                              ></span>
                              <div
                                className="uk-margin-remove"
                                data-uk-drop="mode: click;boundary-align: true; boundary: !.uk-accordion-title; pos: bottom-justify;"
                              >
                                <div className="uk-card uk-card-body uk-card-default uk-card-small uk-box-shadow-xlarge uk-text-small">
                                  A small description for this property
                                </div>
                              </div>
                            </h4>
                            <div className="uk-accordion-content">
                              <ul className="uk-list tm-scrollbox">
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="type-1"
                                    name="type"
                                    value="1"
                                    type="checkbox"
                                  />
                                  <label htmlFor="type-1">
                                    <span>
                                      Notebook
                                      <span className="uk-text-meta uk-text-xsmall">
                                        150
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="type-2"
                                    name="type"
                                    value="2"
                                    type="checkbox"
                                  />
                                  <label htmlFor="type-2">
                                    <span>
                                      Ultrabook
                                      <span className="uk-text-meta uk-text-xsmall">
                                        18
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="type-3"
                                    name="type"
                                    value="3"
                                    type="checkbox"
                                  />
                                  <label htmlFor="type-3">
                                    <span>
                                      Transformer
                                      <span className="uk-text-meta uk-text-xsmall">
                                        6
                                      </span>
                                    </span>
                                  </label>
                                </li>
                              </ul>
                            </div>
                          </section>
                          <section className="uk-card-body js-accordion-section">
                            <h4 className="uk-accordion-title uk-margin-remove">
                              Screen Size
                              <span
                                className="tm-help-icon"
                                data-uk-icon="icon: question; ratio: .75;"
                                onClick="event.stopPropagation();"
                              ></span>
                              <div
                                className="uk-margin-remove"
                                data-uk-drop="mode: click;boundary-align: true; boundary: !.uk-accordion-title; pos: bottom-justify;"
                              >
                                <div className="uk-card uk-card-body uk-card-default uk-card-small uk-box-shadow-xlarge uk-text-small">
                                  A small description for this property
                                </div>
                              </div>
                            </h4>
                            <div className="uk-accordion-content">
                              <ul className="uk-list tm-scrollbox">
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-size-1"
                                    name="screen-size"
                                    value="1"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-size-1">
                                    <span>
                                      11.6&quot; and smaller
                                      <span className="uk-text-meta uk-text-xsmall">
                                        45
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-size-2"
                                    name="screen-size"
                                    value="2"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-size-2">
                                    <span>
                                      12&quot; - 13.5&quot;
                                      <span className="uk-text-meta uk-text-xsmall">
                                        178
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-size-3"
                                    name="screen-size"
                                    value="3"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-size-3">
                                    <span>
                                      14&quot; - 14.5&quot;
                                      <span className="uk-text-meta uk-text-xsmall">
                                        461
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-size-4"
                                    name="screen-size"
                                    value="4"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-size-4">
                                    <span>
                                      15&quot; - 15.6&quot;
                                      <span className="uk-text-meta uk-text-xsmall">
                                        148
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-size-5"
                                    name="screen-size"
                                    value="5"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-size-5">
                                    <span>
                                      17&quot; - 17.3&quot;
                                      <span className="uk-text-meta uk-text-xsmall">
                                        73
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-size-6"
                                    name="screen-size"
                                    value="6"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-size-6">
                                    <span>
                                      18.4&quot; and larger
                                      <span className="uk-text-meta uk-text-xsmall">
                                        54
                                      </span>
                                    </span>
                                  </label>
                                </li>
                              </ul>
                            </div>
                          </section>
                          <section className="uk-card-body js-accordion-section">
                            <h4 className="uk-accordion-title uk-margin-remove">
                              Screen Resolution
                              <span
                                className="tm-help-icon"
                                data-uk-icon="icon: question; ratio: .75;"
                                onClick="event.stopPropagation();"
                              ></span>
                              <div
                                className="uk-margin-remove"
                                data-uk-drop="mode: click;boundary-align: true; boundary: !.uk-accordion-title; pos: bottom-justify;"
                              >
                                <div className="uk-card uk-card-body uk-card-default uk-card-small uk-box-shadow-xlarge uk-text-small">
                                  A small description for this property
                                </div>
                              </div>
                            </h4>
                            <div className="uk-accordion-content">
                              <ul className="uk-list tm-scrollbox">
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-1"
                                    name="screen-resolution"
                                    value="1"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-1">
                                    <span>
                                      3840×2160
                                      <span className="uk-text-meta uk-text-xsmall">
                                        12
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-2"
                                    name="screen-resolution"
                                    value="2"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-2">
                                    <span>
                                      3200×1800&quot;
                                      <span className="uk-text-meta uk-text-xsmall">
                                        12
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-3"
                                    name="screen-resolution"
                                    value="3"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-3">
                                    <span>
                                      2880×1800
                                      <span className="uk-text-meta uk-text-xsmall">
                                        10
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-4"
                                    name="screen-resolution"
                                    value="4"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-4">
                                    <span>
                                      2560×1600
                                      <span className="uk-text-meta uk-text-xsmall">
                                        7
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-5"
                                    name="screen-resolution"
                                    value="5"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-5">
                                    <span>
                                      2560×1440
                                      <span className="uk-text-meta uk-text-xsmall">
                                        13
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-6"
                                    name="screen-resolution"
                                    value="6"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-6">
                                    <span>
                                      1920×1080
                                      <span className="uk-text-meta uk-text-xsmall">
                                        341
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-7"
                                    name="screen-resolution"
                                    value="7"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-7">
                                    <span>
                                      1600×900
                                      <span className="uk-text-meta uk-text-xsmall">
                                        11
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-8"
                                    name="screen-resolution"
                                    value="8"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-8">
                                    <span>
                                      1440×900
                                      <span className="uk-text-meta uk-text-xsmall">
                                        13
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-9"
                                    name="screen-resolution"
                                    value="9"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-9">
                                    <span>
                                      1366×768
                                      <span className="uk-text-meta uk-text-xsmall">
                                        237
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="screen-resolution-10"
                                    name="screen-resolution"
                                    value="10"
                                    type="checkbox"
                                  />
                                  <label htmlFor="screen-resolution-10">
                                    <span>
                                      1024×600
                                      <span className="uk-text-meta uk-text-xsmall">
                                        5
                                      </span>
                                    </span>
                                  </label>
                                </li>
                              </ul>
                            </div>
                          </section>
                          <section className="uk-card-body js-accordion-section">
                            <h4 className="uk-accordion-title uk-margin-remove">
                              CPU
                              <span
                                className="tm-help-icon"
                                data-uk-icon="icon: question; ratio: .75;"
                                onClick="event.stopPropagation();"
                              ></span>
                              <div
                                className="uk-margin-remove"
                                data-uk-drop="mode: click;boundary-align: true; boundary: !.uk-accordion-title; pos: bottom-justify;"
                              >
                                <div className="uk-card uk-card-body uk-card-default uk-card-small uk-box-shadow-xlarge uk-text-small">
                                  A small description for this property
                                </div>
                              </div>
                            </h4>
                            <div className="uk-accordion-content">
                              <ul className="uk-list tm-scrollbox">
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-1"
                                    name="cpu"
                                    value="1"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-1">
                                    <span>
                                      AMD A-series
                                      <span className="uk-text-meta uk-text-xsmall">
                                        102
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-2"
                                    name="cpu"
                                    value="2"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-2">
                                    <span>
                                      AMD E-series
                                      <span className="uk-text-meta uk-text-xsmall">
                                        21
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-3"
                                    name="cpu"
                                    value="3"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-3">
                                    <span>
                                      AMD FX
                                      <span className="uk-text-meta uk-text-xsmall">
                                        1
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-4"
                                    name="cpu"
                                    value="4"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-4">
                                    <span>
                                      AMD Ryzen
                                      <span className="uk-text-meta uk-text-xsmall">
                                        1
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-5"
                                    name="cpu"
                                    value="5"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-5">
                                    <span>
                                      Intel Atom
                                      <span className="uk-text-meta uk-text-xsmall">
                                        8
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-6"
                                    name="cpu"
                                    value="6"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-6">
                                    <span>
                                      Intel Celeron
                                      <span className="uk-text-meta uk-text-xsmall">
                                        38
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-7"
                                    name="cpu"
                                    value="7"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-7">
                                    <span>
                                      Intel Core M
                                      <span className="uk-text-meta uk-text-xsmall">
                                        6
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-8"
                                    name="cpu"
                                    value="8"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-8">
                                    <span>
                                      Intel Core i3
                                      <span className="uk-text-meta uk-text-xsmall">
                                        143
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-9"
                                    name="cpu"
                                    value="9"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-9">
                                    <span>
                                      Intel Core i5
                                      <span className="uk-text-meta uk-text-xsmall">
                                        273
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-10"
                                    name="cpu"
                                    value="10"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-10">
                                    <span>
                                      Intel Core i7
                                      <span className="uk-text-meta uk-text-xsmall">
                                        218
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-11"
                                    name="cpu"
                                    value="11"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-11">
                                    <span>
                                      Intel Xeon
                                      <span className="uk-text-meta uk-text-xsmall">
                                        3
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="cpu-12"
                                    name="cpu"
                                    value="12"
                                    type="checkbox"
                                  />
                                  <label htmlFor="cpu-12">
                                    <span>
                                      Intel Pentium
                                      <span className="uk-text-meta uk-text-xsmall">
                                        86
                                      </span>
                                    </span>
                                  </label>
                                </li>
                              </ul>
                            </div>
                          </section>
                          <section className="uk-card-body js-accordion-section">
                            <h4 className="uk-accordion-title uk-margin-remove">
                              RAM
                              <span
                                className="tm-help-icon"
                                data-uk-icon="icon: question; ratio: .75;"
                                onClick="event.stopPropagation();"
                              ></span>
                              <div
                                className="uk-margin-remove"
                                data-uk-drop="mode: click;boundary-align: true; boundary: !.uk-accordion-title; pos: bottom-justify;"
                              >
                                <div className="uk-card uk-card-body uk-card-default uk-card-small uk-box-shadow-xlarge uk-text-small">
                                  A small description for this property
                                </div>
                              </div>
                            </h4>
                            <div className="uk-accordion-content">
                              <ul className="uk-list tm-scrollbox">
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="ram-1"
                                    name="ram"
                                    value="1"
                                    type="checkbox"
                                  />
                                  <label htmlFor="ram-1">
                                    <span>
                                      2 GB
                                      <span className="uk-text-meta uk-text-xsmall">
                                        17
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="ram-2"
                                    name="ram"
                                    value="2"
                                    type="checkbox"
                                  />
                                  <label htmlFor="ram-2">
                                    <span>
                                      4 GB
                                      <span className="uk-text-meta uk-text-xsmall">
                                        359
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="ram-3"
                                    name="ram"
                                    value="3"
                                    type="checkbox"
                                  />
                                  <label htmlFor="ram-3">
                                    <span>
                                      6 GB
                                      <span className="uk-text-meta uk-text-xsmall">
                                        81
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="ram-4"
                                    name="ram"
                                    value="4"
                                    type="checkbox"
                                  />
                                  <label htmlFor="ram-4">
                                    <span>
                                      8 GB
                                      <span className="uk-text-meta uk-text-xsmall">
                                        346
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="ram-5"
                                    name="ram"
                                    value="5"
                                    type="checkbox"
                                  />
                                  <label htmlFor="ram-5">
                                    <span>
                                      12 GB
                                      <span className="uk-text-meta uk-text-xsmall">
                                        13
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="ram-6"
                                    name="ram"
                                    value="6"
                                    type="checkbox"
                                  />
                                  <label htmlFor="ram-6">
                                    <span>
                                      16 GB
                                      <span className="uk-text-meta uk-text-xsmall">
                                        72
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="ram-7"
                                    name="ram"
                                    value="7"
                                    type="checkbox"
                                  />
                                  <label htmlFor="ram-7">
                                    <span>
                                      24 GB
                                      <span className="uk-text-meta uk-text-xsmall">
                                        1
                                      </span>
                                    </span>
                                  </label>
                                </li>
                                <li>
                                  <input
                                    className="tm-checkbox"
                                    id="ram-8"
                                    name="ram"
                                    value="8"
                                    type="checkbox"
                                  />
                                  <label htmlFor="ram-8">
                                    <span>
                                      32 GB
                                      <span className="uk-text-meta uk-text-xsmall">
                                        11
                                      </span>
                                    </span>
                                  </label>
                                </li>
                              </ul>
                            </div>
                          </section>
                          <div className="uk-card-body">
                            <button className="uk-button uk-button-default uk-width-1-1">
                              <span
                                className="uk-margin-xsmall-right"
                                data-uk-icon="icon: close; ratio: .75;"
                              ></span>
                              Reset all filters
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </aside>
                  <div className="uk-width-expand">
                    <div
                      className="uk-grid-medium uk-child-width-1-1"
                      data-uk-grid
                    >
                      <div>
                        <div className="uk-card uk-card-default uk-card-small tm-ignore-container">
                          <div
                            className="uk-grid-collapse uk-child-width-1-1"
                            id="products"
                            data-uk-grid
                          >
                            <div className="uk-card-header">
                              <div
                                className="uk-grid-small uk-flex-middle"
                                data-uk-grid
                              >
                                <div className="uk-width-1-1 uk-width-expand@s uk-flex uk-flex-center uk-flex-left@s uk-text-small">
                                  <span className="uk-margin-small-right uk-text-muted">
                                    Sort by:
                                  </span>
                                  <ul className="uk-subnav uk-margin-remove">
                                    <li className="uk-active uk-padding-remove">
                                      <a className="uk-text-lowercase" href="#">
                                        relevant
                                        <span
                                          className="uk-margin-xsmall-left"
                                          data-uk-icon="icon: chevron-down; ratio: .5;"
                                        ></span>
                                      </a>
                                    </li>
                                    <li>
                                      <a className="uk-text-lowercase" href="#">
                                        price
                                      </a>
                                    </li>
                                    <li>
                                      <a className="uk-text-lowercase" href="#">
                                        newest
                                      </a>
                                    </li>
                                  </ul>
                                </div>
                                <div className="uk-width-1-1 uk-width-auto@s uk-flex uk-flex-center uk-flex-middle">
                                  <button
                                    className="uk-button uk-button-default uk-button-small uk-hidden@m"
                                    uk-toggle="target: #filters"
                                  >
                                    <span
                                      className="uk-margin-xsmall-right"
                                      data-uk-icon="icon: settings; ratio: .75;"
                                    ></span>
                                    Filters
                                  </button>
                                  <div className="tm-change-view uk-margin-small-left">
                                    <ul
                                      className="uk-subnav uk-iconnav js-change-view"
                                      data-uk-switcher
                                    >
                                      <li>
                                        <a
                                          className="uk-active"
                                          data-view="grid"
                                          data-uk-icon="grid"
                                          uk-tooltip="Grid"
                                        ></a>
                                      </li>
                                      <li>
                                        <a
                                          data-view="list"
                                          data-uk-icon="list"
                                          uk-tooltip="List"
                                        ></a>
                                      </li>
                                    </ul>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div>
                              <div
                                className="uk-grid-collapse uk-child-width-1-3 tm-products-grid js-products-grid"
                                data-uk-grid
                              >
                                <article className="tm-product-card">
                                  <div className="tm-product-card-media">
                                    <div className="tm-ratio tm-ratio-4-3">
                                      <a
                                        className="tm-media-box"
                                        href="/products/product"
                                      >
                                        <div className="tm-product-card-labels">
                                          <span className="uk-label uk-label-warning">
                                            top selling
                                          </span>
                                          <span className="uk-label uk-label-danger">
                                            trade-in
                                          </span>
                                        </div>
                                        <figure className="tm-media-box-wrap">
                                          <img
                                            src="/static/images/products/1/1-medium.jpg"
                                            alt='Apple MacBook Pro 15" Touch Bar MPTU2LL/A 256GB (Silver)'
                                          />
                                        </figure>
                                      </a>
                                    </div>
                                  </div>
                                  <div className="tm-product-card-body">
                                    <div className="tm-product-card-info">
                                      <div className="uk-text-meta uk-margin-xsmall-bottom">
                                        Laptop
                                      </div>
                                      <h3 className="tm-product-card-title">
                                        <a
                                          className="uk-link-heading"
                                          href="/products/product"
                                        >
                                          Apple MacBook Pro 15&quot; Touch Bar
                                          MPTU2LL/A 256GB (Silver)
                                        </a>
                                      </h3>
                                      <ul className="uk-list uk-text-small tm-product-card-properties">
                                        <li>
                                          <span className="uk-text-muted">
                                            Diagonal display:{" "}
                                          </span>
                                          <span>15.4"</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            CPU:{" "}
                                          </span>
                                          <span>Intel®&nbsp;Core™ i7</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            RAM:{" "}
                                          </span>
                                          <span>16&nbsp;GB</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            Video Card:{" "}
                                          </span>
                                          <span>AMD Radeon Pro 555</span>
                                        </li>
                                      </ul>
                                    </div>
                                    <div className="tm-product-card-shop">
                                      <div className="tm-product-card-prices">
                                        <del className="uk-text-meta">
                                          $1899.00
                                        </del>
                                        <div className="tm-product-card-price">
                                          $1599.00
                                        </div>
                                      </div>
                                      <div className="tm-product-card-add">
                                        <div className="uk-text-meta tm-product-card-actions">
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-favorites tm-action-button-active js-added-to"
                                            title="Add to favorites"
                                          >
                                            <span data-uk-icon="icon: heart; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to favorites
                                            </span>
                                          </a>
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-compare tm-action-button-active js-added-to"
                                            title="Add to compare"
                                          >
                                            <span data-uk-icon="icon: copy; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to compare
                                            </span>
                                          </a>
                                        </div>
                                        <button className="uk-button uk-button-primary tm-product-card-add-button tm-shine js-add-to-cart">
                                          <span
                                            className="tm-product-card-add-button-icon"
                                            data-uk-icon="cart"
                                          ></span>
                                          <span className="tm-product-card-add-button-text">
                                            add to cart
                                          </span>
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </article>
                                <article className="tm-product-card">
                                  <div className="tm-product-card-media">
                                    <div className="tm-ratio tm-ratio-4-3">
                                      <a
                                        className="tm-media-box"
                                        href="/products/product"
                                      >
                                        <div className="tm-product-card-labels">
                                          <span className="uk-label uk-label-success">
                                            new
                                          </span>
                                          <span className="uk-label uk-label-danger">
                                            trade-in
                                          </span>
                                        </div>
                                        <figure className="tm-media-box-wrap">
                                          <img
                                            src="/static/images/products/2/2-medium.jpg"
                                            alt='Apple MacBook 12" MNYN2LL/A 512GB (Rose Gold)'
                                          />
                                        </figure>
                                      </a>
                                    </div>
                                  </div>
                                  <div className="tm-product-card-body">
                                    <div className="tm-product-card-info">
                                      <div className="uk-text-meta uk-margin-xsmall-bottom">
                                        Laptop
                                      </div>
                                      <h3 className="tm-product-card-title">
                                        <a
                                          className="uk-link-heading"
                                          href="/products/product"
                                        >
                                          Apple MacBook 12&quot; MNYN2LL/A 512GB
                                          (Rose Gold)
                                        </a>
                                      </h3>
                                      <ul className="uk-list uk-text-small tm-product-card-properties">
                                        <li>
                                          <span className="uk-text-muted">
                                            Diagonal display:{" "}
                                          </span>
                                          <span>12"</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            CPU:{" "}
                                          </span>
                                          <span>Intel®&nbsp;Core™ i5</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            RAM:{" "}
                                          </span>
                                          <span>8&nbsp;GB</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            Video Card:{" "}
                                          </span>
                                          <span>Intel® HD Graphics 615</span>
                                        </li>
                                      </ul>
                                    </div>
                                    <div className="tm-product-card-shop">
                                      <div className="tm-product-card-prices">
                                        <div className="tm-product-card-price">
                                          $1549.00
                                        </div>
                                      </div>
                                      <div className="tm-product-card-add">
                                        <div className="uk-text-meta tm-product-card-actions">
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-favorites tm-action-button-active js-added-to"
                                            title="Add to favorites"
                                          >
                                            <span data-uk-icon="icon: heart; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to favorites
                                            </span>
                                          </a>
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-compare tm-action-button-active js-added-to"
                                            title="Add to compare"
                                          >
                                            <span data-uk-icon="icon: copy; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to compare
                                            </span>
                                          </a>
                                        </div>
                                        <button className="uk-button uk-button-primary tm-product-card-add-button tm-shine js-add-to-cart">
                                          <span
                                            className="tm-product-card-add-button-icon"
                                            data-uk-icon="cart"
                                          ></span>
                                          <span className="tm-product-card-add-button-text">
                                            add to cart
                                          </span>
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </article>
                                <article className="tm-product-card">
                                  <div className="tm-product-card-media">
                                    <div className="tm-ratio tm-ratio-4-3">
                                      <a
                                        className="tm-media-box"
                                        href="/products/product"
                                      >
                                        <figure className="tm-media-box-wrap">
                                          <img
                                            src="/static/images/products/3/3-medium.jpg"
                                            alt="Lenovo IdeaPad YOGA 920-13IKB 80Y7001RRK (Copper)"
                                          />
                                        </figure>
                                      </a>
                                    </div>
                                  </div>
                                  <div className="tm-product-card-body">
                                    <div className="tm-product-card-info">
                                      <div className="uk-text-meta uk-margin-xsmall-bottom">
                                        Laptop
                                      </div>
                                      <h3 className="tm-product-card-title">
                                        <a
                                          className="uk-link-heading"
                                          href="/products/product"
                                        >
                                          Lenovo IdeaPad YOGA 920-13IKB
                                          80Y7001RRK (Copper)
                                        </a>
                                      </h3>
                                      <ul className="uk-list uk-text-small tm-product-card-properties">
                                        <li>
                                          <span className="uk-text-muted">
                                            Diagonal display:{" "}
                                          </span>
                                          <span>13.9"</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            CPU:{" "}
                                          </span>
                                          <span>
                                            Intel®&nbsp;Core™ i7 8550U
                                          </span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            RAM:{" "}
                                          </span>
                                          <span>16&nbsp;GB</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            Video Card:{" "}
                                          </span>
                                          <span>Intel® HD Graphics 620</span>
                                        </li>
                                      </ul>
                                    </div>
                                    <div className="tm-product-card-shop">
                                      <div className="tm-product-card-prices">
                                        <div className="tm-product-card-price">
                                          $1199.00
                                        </div>
                                      </div>
                                      <div className="tm-product-card-add">
                                        <div className="uk-text-meta tm-product-card-actions">
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-favorites tm-action-button-active js-added-to"
                                            title="Add to favorites"
                                          >
                                            <span data-uk-icon="icon: heart; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to favorites
                                            </span>
                                          </a>
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-compare"
                                            title="Add to compare"
                                          >
                                            <span data-uk-icon="icon: copy; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to compare
                                            </span>
                                          </a>
                                        </div>
                                        <button className="uk-button uk-button-primary tm-product-card-add-button tm-shine js-add-to-cart">
                                          <span
                                            className="tm-product-card-add-button-icon"
                                            data-uk-icon="cart"
                                          ></span>
                                          <span className="tm-product-card-add-button-text">
                                            add to cart
                                          </span>
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </article>
                                <article className="tm-product-card">
                                  <div className="tm-product-card-media">
                                    <div className="tm-ratio tm-ratio-4-3">
                                      <a
                                        className="tm-media-box"
                                        href="/products/product"
                                      >
                                        <div className="tm-product-card-labels">
                                          <span className="uk-label uk-label-warning">
                                            top selling
                                          </span>
                                        </div>
                                        <figure className="tm-media-box-wrap">
                                          <img
                                            src="/static/images/products/4/4-medium.jpg"
                                            alt="ASUS Zenbook UX330UA-FC020T (Rose Gold)"
                                          />
                                        </figure>
                                      </a>
                                    </div>
                                  </div>
                                  <div className="tm-product-card-body">
                                    <div className="tm-product-card-info">
                                      <div className="uk-text-meta uk-margin-xsmall-bottom">
                                        Laptop
                                      </div>
                                      <h3 className="tm-product-card-title">
                                        <a
                                          className="uk-link-heading"
                                          href="/products/product"
                                        >
                                          ASUS Zenbook UX330UA-FC020T (Rose
                                          Gold)
                                        </a>
                                      </h3>
                                      <ul className="uk-list uk-text-small tm-product-card-properties">
                                        <li>
                                          <span className="uk-text-muted">
                                            Diagonal display:{" "}
                                          </span>
                                          <span>13.3"</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            CPU:{" "}
                                          </span>
                                          <span>
                                            Intel®&nbsp;Core™ i7-6500U
                                          </span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            RAM:{" "}
                                          </span>
                                          <span>8&nbsp;GB</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            Video Card:{" "}
                                          </span>
                                          <span>Intel® HD Graphics 520</span>
                                        </li>
                                      </ul>
                                    </div>
                                    <div className="tm-product-card-shop">
                                      <div className="tm-product-card-prices">
                                        <div className="tm-product-card-price">
                                          $749.00
                                        </div>
                                      </div>
                                      <div className="tm-product-card-add">
                                        <div className="uk-text-meta tm-product-card-actions">
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-favorites"
                                            title="Add to favorites"
                                          >
                                            <span data-uk-icon="icon: heart; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to favorites
                                            </span>
                                          </a>
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-compare"
                                            title="Add to compare"
                                          >
                                            <span data-uk-icon="icon: copy; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to compare
                                            </span>
                                          </a>
                                        </div>
                                        <button className="uk-button uk-button-primary tm-product-card-add-button tm-shine js-add-to-cart">
                                          <span
                                            className="tm-product-card-add-button-icon"
                                            data-uk-icon="cart"
                                          ></span>
                                          <span className="tm-product-card-add-button-text">
                                            add to cart
                                          </span>
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </article>
                                <article className="tm-product-card">
                                  <div className="tm-product-card-media">
                                    <div className="tm-ratio tm-ratio-4-3">
                                      <a
                                        className="tm-media-box"
                                        href="/products/product"
                                      >
                                        <figure className="tm-media-box-wrap">
                                          <img
                                            src="/static/images/products/5/5-medium.jpg"
                                            alt="Dell XPS 15 9560-8968 (Silver)"
                                          />
                                        </figure>
                                      </a>
                                    </div>
                                  </div>
                                  <div className="tm-product-card-body">
                                    <div className="tm-product-card-info">
                                      <div className="uk-text-meta uk-margin-xsmall-bottom">
                                        Laptop
                                      </div>
                                      <h3 className="tm-product-card-title">
                                        <a
                                          className="uk-link-heading"
                                          href="/products/product"
                                        >
                                          Dell XPS 15 9560-8968 (Silver)
                                        </a>
                                      </h3>
                                      <ul className="uk-list uk-text-small tm-product-card-properties">
                                        <li>
                                          <span className="uk-text-muted">
                                            Diagonal display:{" "}
                                          </span>
                                          <span>15.6"</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            CPU:{" "}
                                          </span>
                                          <span>
                                            Intel®&nbsp;Core™ i7 7700HQ
                                          </span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            RAM:{" "}
                                          </span>
                                          <span>16&nbsp;GB</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            Video Card:{" "}
                                          </span>
                                          <span>NVIDIA GeForce GTX 960M</span>
                                        </li>
                                      </ul>
                                    </div>
                                    <div className="tm-product-card-shop">
                                      <div className="tm-product-card-prices">
                                        <del className="uk-text-meta">
                                          $999.00
                                        </del>
                                        <div className="tm-product-card-price">
                                          $949.00
                                        </div>
                                      </div>
                                      <div className="tm-product-card-add">
                                        <div className="uk-text-meta tm-product-card-actions">
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-favorites"
                                            title="Add to favorites"
                                          >
                                            <span data-uk-icon="icon: heart; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to favorites
                                            </span>
                                          </a>
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-compare"
                                            title="Add to compare"
                                          >
                                            <span data-uk-icon="icon: copy; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to compare
                                            </span>
                                          </a>
                                        </div>
                                        <button className="uk-button uk-button-primary tm-product-card-add-button tm-shine js-add-to-cart">
                                          <span
                                            className="tm-product-card-add-button-icon"
                                            data-uk-icon="cart"
                                          ></span>
                                          <span className="tm-product-card-add-button-text">
                                            add to cart
                                          </span>
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </article>
                                <article className="tm-product-card">
                                  <div className="tm-product-card-media">
                                    <div className="tm-ratio tm-ratio-4-3">
                                      <a
                                        className="tm-media-box"
                                        href="/products/product"
                                      >
                                        <div className="tm-product-card-labels">
                                          <span className="uk-label uk-label-danger">
                                            trade-in
                                          </span>
                                        </div>
                                        <figure className="tm-media-box-wrap">
                                          <img
                                            src="/static/images/products/6/6-medium.jpg"
                                            alt='Apple MacBook Air 13" MQD32LL/A 128GB (Silver)'
                                          />
                                        </figure>
                                      </a>
                                    </div>
                                  </div>
                                  <div className="tm-product-card-body">
                                    <div className="tm-product-card-info">
                                      <div className="uk-text-meta uk-margin-xsmall-bottom">
                                        Laptop
                                      </div>
                                      <h3 className="tm-product-card-title">
                                        <a
                                          className="uk-link-heading"
                                          href="/products/product"
                                        >
                                          Apple MacBook Air 13&quot; MQD32LL/A
                                          128GB (Silver)
                                        </a>
                                      </h3>
                                      <ul className="uk-list uk-text-small tm-product-card-properties">
                                        <li>
                                          <span className="uk-text-muted">
                                            Diagonal display:{" "}
                                          </span>
                                          <span>13.3"</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            CPU:{" "}
                                          </span>
                                          <span>Intel®&nbsp;Core™ i5</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            RAM:{" "}
                                          </span>
                                          <span>8&nbsp;GB</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            Video Card:{" "}
                                          </span>
                                          <span>Intel® HD Graphics 6000</span>
                                        </li>
                                      </ul>
                                    </div>
                                    <div className="tm-product-card-shop">
                                      <div className="tm-product-card-prices">
                                        <div className="tm-product-card-price">
                                          $849.00
                                        </div>
                                      </div>
                                      <div className="tm-product-card-add">
                                        <div className="uk-text-meta tm-product-card-actions">
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-favorites"
                                            title="Add to favorites"
                                          >
                                            <span data-uk-icon="icon: heart; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to favorites
                                            </span>
                                          </a>
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-compare tm-action-button-active js-added-to"
                                            title="Add to compare"
                                          >
                                            <span data-uk-icon="icon: copy; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to compare
                                            </span>
                                          </a>
                                        </div>
                                        <button className="uk-button uk-button-primary tm-product-card-add-button tm-shine js-add-to-cart">
                                          <span
                                            className="tm-product-card-add-button-icon"
                                            data-uk-icon="cart"
                                          ></span>
                                          <span className="tm-product-card-add-button-text">
                                            add to cart
                                          </span>
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </article>
                                <article className="tm-product-card">
                                  <div className="tm-product-card-media">
                                    <div className="tm-ratio tm-ratio-4-3">
                                      <a
                                        className="tm-media-box"
                                        href="/products/product"
                                      >
                                        <figure className="tm-media-box-wrap">
                                          <img
                                            src="/static/images/products/7/7-medium.jpg"
                                            alt="Dell Inspiron 5378-2063 (Gray)"
                                          />
                                        </figure>
                                      </a>
                                    </div>
                                  </div>
                                  <div className="tm-product-card-body">
                                    <div className="tm-product-card-info">
                                      <div className="uk-text-meta uk-margin-xsmall-bottom">
                                        Laptop
                                      </div>
                                      <h3 className="tm-product-card-title">
                                        <a
                                          className="uk-link-heading"
                                          href="/products/product"
                                        >
                                          Dell Inspiron 5378-2063 (Gray)
                                        </a>
                                      </h3>
                                      <ul className="uk-list uk-text-small tm-product-card-properties">
                                        <li>
                                          <span className="uk-text-muted">
                                            Diagonal display:{" "}
                                          </span>
                                          <span>13.3"</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            CPU:{" "}
                                          </span>
                                          <span>
                                            Intel®&nbsp;Core™ i3-7100U
                                          </span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            RAM:{" "}
                                          </span>
                                          <span>4&nbsp;GB</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            HDD Capacity:{" "}
                                          </span>
                                          <span>1&nbsp;TB</span>
                                        </li>
                                      </ul>
                                    </div>
                                    <div className="tm-product-card-shop">
                                      <div className="tm-product-card-prices">
                                        <del className="uk-text-meta">
                                          $599.00
                                        </del>
                                        <div className="tm-product-card-price">
                                          $579.00
                                        </div>
                                      </div>
                                      <div className="tm-product-card-add">
                                        <div className="uk-text-meta tm-product-card-actions">
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-favorites"
                                            title="Add to favorites"
                                          >
                                            <span data-uk-icon="icon: heart; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to favorites
                                            </span>
                                          </a>
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-compare"
                                            title="Add to compare"
                                          >
                                            <span data-uk-icon="icon: copy; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to compare
                                            </span>
                                          </a>
                                        </div>
                                        <button className="uk-button uk-button-primary tm-product-card-add-button tm-shine js-add-to-cart">
                                          <span
                                            className="tm-product-card-add-button-icon"
                                            data-uk-icon="cart"
                                          ></span>
                                          <span className="tm-product-card-add-button-text">
                                            add to cart
                                          </span>
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </article>
                                <article className="tm-product-card">
                                  <div className="tm-product-card-media">
                                    <div className="tm-ratio tm-ratio-4-3">
                                      <a
                                        className="tm-media-box"
                                        href="/products/product"
                                      >
                                        <div className="tm-product-card-labels">
                                          <span className="uk-label uk-label-success">
                                            new
                                          </span>
                                        </div>
                                        <figure className="tm-media-box-wrap">
                                          <img
                                            src="/static/images/products/8/8-medium.jpg"
                                            alt="Lenovo Yoga 720-13IKB 80X60059RK (Silver)"
                                          />
                                        </figure>
                                      </a>
                                    </div>
                                  </div>
                                  <div className="tm-product-card-body">
                                    <div className="tm-product-card-info">
                                      <div className="uk-text-meta uk-margin-xsmall-bottom">
                                        Laptop
                                      </div>
                                      <h3 className="tm-product-card-title">
                                        <a
                                          className="uk-link-heading"
                                          href="/products/product"
                                        >
                                          Lenovo Yoga 720-13IKB 80X60059RK
                                          (Silver)
                                        </a>
                                      </h3>
                                      <ul className="uk-list uk-text-small tm-product-card-properties">
                                        <li>
                                          <span className="uk-text-muted">
                                            Diagonal display:{" "}
                                          </span>
                                          <span>13.3"</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            CPU:{" "}
                                          </span>
                                          <span>
                                            Intel®&nbsp;Core™ i5-7200U
                                          </span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            RAM:{" "}
                                          </span>
                                          <span>8&nbsp;GB</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            Video Card:{" "}
                                          </span>
                                          <span>Intel® HD Graphics 620</span>
                                        </li>
                                      </ul>
                                    </div>
                                    <div className="tm-product-card-shop">
                                      <div className="tm-product-card-prices">
                                        <div className="tm-product-card-price">
                                          $1099.00
                                        </div>
                                      </div>
                                      <div className="tm-product-card-add">
                                        <div className="uk-text-meta tm-product-card-actions">
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-favorites"
                                            title="Add to favorites"
                                          >
                                            <span data-uk-icon="icon: heart; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to favorites
                                            </span>
                                          </a>
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-compare"
                                            title="Add to compare"
                                          >
                                            <span data-uk-icon="icon: copy; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to compare
                                            </span>
                                          </a>
                                        </div>
                                        <button className="uk-button uk-button-primary tm-product-card-add-button tm-shine js-add-to-cart">
                                          <span
                                            className="tm-product-card-add-button-icon"
                                            data-uk-icon="cart"
                                          ></span>
                                          <span className="tm-product-card-add-button-text">
                                            add to cart
                                          </span>
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </article>
                                <article className="tm-product-card">
                                  <div className="tm-product-card-media">
                                    <div className="tm-ratio tm-ratio-4-3">
                                      <a
                                        className="tm-media-box"
                                        href="/products/product"
                                      >
                                        <figure className="tm-media-box-wrap">
                                          <span
                                            className="uk-text-muted"
                                            data-uk-icon="icon: image; ratio: 3;"
                                          ></span>
                                        </figure>
                                      </a>
                                    </div>
                                  </div>
                                  <div className="tm-product-card-body">
                                    <div className="tm-product-card-info">
                                      <div className="uk-text-meta uk-margin-xsmall-bottom">
                                        Laptop
                                      </div>
                                      <h3 className="tm-product-card-title">
                                        <a
                                          className="uk-link-heading"
                                          href="/products/product"
                                        >
                                          Lenovo ThinkPad X380 Yoga 20LH000MUS
                                          (Black)
                                        </a>
                                      </h3>
                                      <ul className="uk-list uk-text-small tm-product-card-properties">
                                        <li>
                                          <span className="uk-text-muted">
                                            Diagonal display:{" "}
                                          </span>
                                          <span>13.3"</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            CPU:{" "}
                                          </span>
                                          <span>
                                            Intel®&nbsp;Core™ i7 8550U
                                          </span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            RAM:{" "}
                                          </span>
                                          <span>4&nbsp;GB</span>
                                        </li>
                                        <li>
                                          <span className="uk-text-muted">
                                            Video Card:{" "}
                                          </span>
                                          <span>Intel® UHD Graphics 620</span>
                                        </li>
                                      </ul>
                                    </div>
                                    <div className="tm-product-card-shop">
                                      <div className="tm-product-card-prices">
                                        <div className="uk-text-muted">
                                          Product not available
                                        </div>
                                      </div>
                                      <div className="tm-product-card-add">
                                        <div className="uk-text-meta tm-product-card-actions">
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-favorites"
                                            title="Add to favorites"
                                          >
                                            <span data-uk-icon="icon: heart; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to favorites
                                            </span>
                                          </a>
                                          <a
                                            className="tm-product-card-action js-add-to js-add-to-compare"
                                            title="Add to compare"
                                          >
                                            <span data-uk-icon="icon: copy; ratio: .75;"></span>
                                            <span className="tm-product-card-action-text">
                                              Add to compare
                                            </span>
                                          </a>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </article>
                              </div>
                            </div>
                            <div>
                              <button
                                className="uk-button uk-button-default uk-button-large uk-width-1-1"
                                style={{
                                  borderTopLeftRadius: 0,
                                  borderTopRightRadius: 0,
                                }}
                              >
                                <span
                                  className="uk-margin-small-right"
                                  data-uk-icon="icon: plus; ratio: .75;"
                                ></span>
                                <span>Load more</span>
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div>
                        <ul className="uk-pagination uk-flex-center">
                          <li className="uk-active">
                            <span>1</span>
                          </li>
                          <li>
                            <a href="#">2</a>
                          </li>
                          <li>
                            <a href="#">3</a>
                          </li>
                          <li>
                            <a href="#">4</a>
                          </li>
                          <li>
                            <a href="#">5</a>
                          </li>
                          <li className="uk-disabled">
                            <span>…</span>
                          </li>
                          <li>
                            <a href="#">20</a>
                          </li>
                          <li>
                            <a href="#">
                              <span data-uk-pagination-next></span>
                            </a>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    );
  }
}

ReactDOM.render(
    <SubCategory bahs={window.bah}/>,
    document.getElementById("subcategory-page")
);
