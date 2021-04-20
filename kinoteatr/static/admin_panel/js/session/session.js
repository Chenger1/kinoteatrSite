function handleMovie(pk, name, img_path){
    let my_modal = $('#movieModal');
    let chosen_movie = $('#chose_movie');
    let selected_movie = $('#selected_movie')
    let movie_image = $('#show_main_image');

    $(chosen_movie).text(name);
    $(selected_movie).attr('value', pk);
    $(movie_image).attr('src', img_path);
}