KindEditor.ready(function(K) {
        window.editor = K.create('textarea[name=text]', {
        // K.create('#id_text', {
            resizeType:1,
            allowPreviewEmoticons : false,
            allowImageRemote : false,
            uploadJson : '/admin/upload/kindeditor',
            width: '800px',
            height: '800px',

        });
});
