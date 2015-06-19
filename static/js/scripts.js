$(document).ready(function() {
    $(document).foundation();

    // Isotopes.

    $('.b-cards-wrapper').isotope({
        itemSelector: '.b-card',
        layoutMode: 'fitRows'
    });

    if (getQuery('search')) {
        var filterValue = '[data-filters*=' + slugy(getQuery('search')) + ']';

        $('.b-search-field').val(slugy(getQuery('search')).replace('-', ' '));
        $('.b-cards-wrapper').isotope({ filter: filterValue });

    } else if (getQuery('cat')) {
        $('.b-cards-wrapper').isotope({ filter:  '.m-' + getQuery('cat') });
    }

    $('.b-search-repo .b-button').click(function() {
        var txt = slugy($('.b-search-repo .b-search-field').val());

        txt = txt ? '[data-filters*=' + txt + ']' : '*';

        $('.b-cards-wrapper').isotope({ filter: txt });

        return false;
    });

    $('.b-main-category-menu-repo .e-main-category').click(function() {
        var filterValue = $(this).data('filter');

        $('.b-cards-wrapper').isotope({ filter: filterValue });

        return false;
    });

    $('.e-filter-tag').click(function() {
        var filterValue = '';

        $(this).toggleClass('m-active');

        $('.e-filter-tag.m-active').each(function() {
            filterValue += $(this).attr('data-filter');
        });

        $('.b-cards-wrapper').isotope({ filter: filterValue || '*'});

        return false;
    });

    // Off Canvas Menu

    $('.b-offcanvas .b-item-wrapper').slideUp();

    $('.b-main-section').swipe({
        swipeRight: function () {
            $('.b-content').foundation('offcanvas', 'show', 'move-right');

            return false;
        },

        excludedElements: ''
    });

    $('.b-offcanvas').swipe({
        swipeLeft: function () {
            $('.b-content').foundation('offcanvas', 'hide', 'move-right');

            return false;
        }
    });

    $('.b-profile').swipe({
        swipeLeft: function () {
            $('.reveal-modal.open').foundation('reveal', 'close');

            return false;
        },

        swipeRight: function () {
            $('.reveal-modal.open').foundation('reveal', 'close');

            return false;
        }
    });

    $('.b-offcanvas .m-filter-name').click(function() {
        if ($(this).children().hasClass('fa-plus')) {
            $(this).addClass('m-active');
            $(this).children().removeClass('fa-plus');
            $(this).children().addClass('fa-minus');

            $(this).next().slideDown();

        } else {
            $(this).removeClass('m-active');
            $(this).children().removeClass('fa-minus');
            $(this).children().addClass('fa-plus');

            $(this).next().slideUp();
        }
    });

    $(document).on('open.fndtn.offcanvas', '[data-offcanvas]', function() {
        $('.left-off-canvas-toggle').addClass('m-active');
        $('.inner-wrap').height($('.b-offcanvas')[0].scrollHeight);
    });

    $(document).on('close.fndtn.offcanvas', '[data-offcanvas]', function() {
        $('.left-off-canvas-toggle').removeClass('m-active');
        $('.inner-wrap').height('auto');
    });

    $('.e-mainnav-trigger').click(function() {
        var trigger = $(this);

        if(trigger.hasClass('m-nav-active')) {
            trigger.removeClass('m-nav-active');
            trigger.parent().removeClass('m-nav-active');

        } else {
            trigger.addClass('m-nav-active');
            trigger.parent().addClass('m-nav-active');
        }
    });

    $('#overlay').click(function() {
        $(this).removeClass('m-active');
        $('.b-filters').removeClass('m-active');
    });

    // RSS from Digest
    $('#blog-container').rssfeed('http://thegovlab.org/researchrepo/feed/', {
        limit: 10,
        linktarget: '_blank',
        content: true,
        media: true
    });

    $('#digest-container').rssfeed('http://thegovlab.org/govlab-digest/feed/',
    {
        limit: 10,
        linktarget: '_blank',
        content: true,
        media: true
    });
 });

function getQuery(param) {
    var query = location.search.substr(1),
        result = false;

    query.split('&').forEach(function(part) {
        var item = part.split('=');

        if (item[0] == param) {
            result = decodeURIComponent(item[1]);

            if (result.slice(-1) == '/') {
                result = result.slice(0, -1);
            }
        }
    });

    return result;
}

function slugy(value) {
    var reg1 = /[\u0300-\u036F]/g; // Use XRegExp('\\p{M}', 'g');
    var reg2 = /\s+/g;

    // The "$.data('attribute')" is commonly used as a source for the
    // "value" parameter, and it will convert digit only strings to
    // numbers. The "value.toString()" call will prevent failure in
    // this case, and whenever "value" is not a string.
    //
    value = value.toString().toLowerCase().trim().replace('+', ' ');

    return unorm.nfkd(value).replace(reg1, '').replace(reg2, '-');
}
