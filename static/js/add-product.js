/* Add Product form style */

function add_product() {
    let discount_field = document.getElementById('id_discount');
    let add_productfield1 = document.getElementById('id_price');
    let add_productfield2 = document.getElementById('id_weight');
    let add_productfield3 = document.getElementById('id_description');
    let add_productfield4 = document.getElementById('id_dimension');
    let add_productfield5 = document.getElementById('id_sku');

    if (discount_field !== null) {
        discount_field.placeholder = 'Leave blank for no discount', discount_field.className += ' text-dark shadow-none';

        discount_field.style.width = '100%';
        discount_field.style.height = '50px';
    };

    if (add_productfield1 !== null) {
        add_productfield1.placeholder = '20.00', discount_field.className += ' text-dark shadow-none';

        discount_field.style.width = '100%';
        discount_field.style.height = '50px';
    };

    if (add_productfield2 !== null) {
        add_productfield2.placeholder = '0.5', discount_field.className += ' text-dark shadow-none';

        discount_field.style.width = '100%';
        discount_field.style.height = '50px';
    };

    if (add_productfield3 !== null) {
        add_productfield3.placeholder = 'Describe the product', discount_field.className += ' text-dark shadow-none';

        discount_field.style.width = '100%';
        discount_field.style.height = '50px';
    };

    if (add_productfield4 !== null) {
        add_productfield4.placeholder = 'Width 6.5 cm Depth 15.5 cm Height 27.4 cm', discount_field.className += ' text-dark shadow-none';

        discount_field.style.width = '100%';
        discount_field.style.height = '50px';
    };

    if (add_productfield5 !== null) {
        add_productfield5.placeholder = 'Enter Product SKU', discount_field.className += ' text-dark shadow-none';

        discount_field.style.width = '100%';
        discount_field.style.height = '50px';
    };
}
add_product()