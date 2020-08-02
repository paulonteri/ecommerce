import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import { AddToCart } from "../../../frontend/static/js/header";

class Category extends Component {
  constructor(props) {
    super(props);

    //
    const categoryData = JSON.parse(
      document.getElementById("categoryData").textContent
    );
    const websiteName = JSON.parse(
      document.getElementById("websiteName").textContent
    );

    //
    this.state = {
      slug: categoryData.slug,
      title: categoryData.title,
      categoryTitle: "value",
      // categorySlug: categoryData.category__slug,
      categorySlug: "value",
      subCategories: categoryData.subcategories,
      brands: categoryData.brands,
      items: categoryData.items,
      websiteName: websiteName,
    };
  }

  componentDidMount() {
    //
  }

  handleBrandSelect(value) {
    console.log(value);
  }

  handleSubCategorySelect(value) {
    console.log(value);
  }

  handleResetFilters() {
    //
  }

  AsideContent() {
    const { brands, subCategories } = this.state;

    return (
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
                <h4 className="uk-accordion-title uk-margin-remove">Prices</h4>
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
                        <span className="uk-form-icon uk-text-xsmall">to</span>
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
              {/* ///////////////////// */}
              <section className="uk-card-body js-accordion-section uk-open">
                <h4 className="uk-accordion-title uk-margin-remove">
                  Sub Categories
                </h4>
                <button
                  onClick={() =>
                    sessionStorage.setItem(
                      "cartNumber",
                      parseInt(sessionStorage.getItem("cartNumber")) + 5
                    )
                  }
                >
                  Add to cart
                </button>
                <div className="uk-accordion-content">
                  <ul className="uk-list tm-scrollbox uk-text-capitalize">
                    {subCategories.map((subCategory) => {
                      return (
                        <li key={subCategory.title}>
                          <input
                            className="tm-checkbox"
                            id={subCategory.title}
                            value={subCategory.title}
                            name="subCategory"
                            type="checkbox"
                            onClick={() =>
                              this.handleSubCategorySelect(subCategory.title)
                            }
                          />
                          <label htmlFor={subCategory.title}>
                            <span>{subCategory.title}</span>
                          </label>
                        </li>
                      );
                    })}
                  </ul>
                </div>
              </section>
              {/* ///////////////////// */}
              <section className="uk-card-body js-accordion-section uk-open">
                <h4 className="uk-accordion-title uk-margin-remove">Brands</h4>
                <div className="uk-accordion-content">
                  <ul className="uk-list tm-scrollbox">
                    {brands.map((brand) => {
                      return (
                        <li key={brand.title}>
                          <input
                            className="tm-checkbox"
                            id={brand.title}
                            value={brand.title}
                            name="brand"
                            type="checkbox"
                            onClick={() => this.handleBrandSelect(brand.title)}
                          />
                          <label htmlFor={brand.title}>
                            <span>{brand.title}</span>
                          </label>
                        </li>
                      );
                    })}
                  </ul>
                </div>
              </section>

              <div className="uk-card-body">
                <button
                  className="uk-button uk-button-default uk-width-1-1"
                  onClick={() => this.handleResetFilters()}
                >
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
    );
  }

  ProductCards() {
    const { title, items, websiteName } = this.state;

    return (
      <Fragment>
        {items.map((item) => {
          return (
            <article
              className="tm-product-card uk-first-column"
              key={item.slug}
            >
              <div className="tm-product-card-media">
                <div className="tm-ratio tm-ratio-4-3">
                  <a
                    className="tm-media-box"
                    href={"/products/product/" + item.slug}
                  >
                    <div className="tm-product-card-labels">
                      <span className="uk-label uk-label-warning">
                        top selling
                      </span>
                    </div>

                    <figure className="tm-media-box-wrap">
                      <img
                        src={item.image}
                        alt={title + " from " + websiteName}
                      />
                    </figure>
                  </a>
                </div>
              </div>

              <div className="tm-product-card-body">
                <div className="tm-product-card-info">
                  <div className="uk-text-meta uk-margin-xsmall-bottom uk-text-capitalize">
                    {item.sub_category__title}
                  </div>

                  <h3 className="tm-product-card-title">
                    <a
                      className="uk-link-heading"
                      href={"/products/product/" + item.slug}
                    >
                      {item.title}
                    </a>
                  </h3>
                </div>
                <div className="tm-product-card-shop">
                  <div className="tm-product-card-prices">
                    <del className="uk-text-meta">$1899.00</del>
                    <div className="tm-product-card-price">{item.price}</div>
                  </div>
                  <AddToCart />
                </div>
              </div>
            </article>
          );
        })}
      </Fragment>
    );
  }

  render() {
    console.log(this.state);
    const { title, categorySlug, categoryTitle } = this.state;
    return (
      <main>
        <section className="uk-section uk-section-small">
          <div className="uk-container">
            <div className="uk-grid-medium uk-child-width-1-1" data-uk-grid>
              {/* <--------------------   Title   -------------------> */}
              <div className="uk-text-center">
                <ul className="uk-breadcrumb uk-flex-center uk-margin-remove uk-text-capitalize">
                  <li>
                    <a href="/">Home</a>
                  </li>
                  <li>
                    <a href="/products/catalog">Catalog</a>
                  </li>

                  <li>
                    <span className="uk-text-capitalize">{title}</span>
                  </li>
                </ul>
                <h1 className="uk-margin-small-top uk-margin-remove-bottom uk-text-capitalize">
                  {title}
                </h1>
              </div>
              {/* <--------------------   End Title   -------------------> */}
              <div>
                <div className="uk-grid-medium" data-uk-grid>
                  {/* ------------------------ Aside ------------------ */}
                  {this.AsideContent()}
                  {/* ------------------------ End Aside ------------------ */}
                  {/* -------------------  All Items ---------------------- */}
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
                              {/* ---------------------------------- Items ------------------------------- */}
                              <div
                                className="uk-grid-collapse uk-child-width-1-3 tm-products-grid js-products-grid"
                                data-uk-grid
                              >
                                {/* ------------------------ ProductCards ------------------ */}
                                {this.ProductCards()}
                                {/* ------------------------ End ProductCards ------------------ */}
                              </div>
                              {/* ---------------------------------- End Items ------------------------------- */}
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

ReactDOM.render(<Category />, document.getElementById("category-page"));
