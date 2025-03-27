CKEDITOR.editorConfig = function(config) {
    config.language = 'en';
    config.toolbar = [
        { name: 'basicstyles', items: ['Bold', 'Italic', 'Underline'] },
        { name: 'links', items: ['Link', 'Unlink'] },
        { name: 'insert', items: ['Image', 'Table'] },
        { name: 'styles', items: ['Styles', 'Format'] },
        { name: 'colors', items: ['TextColor', 'BGColor'] },
    ];
    config.removePlugins = 'elementspath';
    config.resize_enabled = false;
};