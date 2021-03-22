#include <stdio.h>
#include <stdlib.h>
#include <SFML/Graphics.h>
#include <SFML/System.h>
#include <SFML/Window.h>
#include <SFML/Audio.h>

int main(int ac, char *av[])
{
    if (ac != 2) {
        printf("Speed pls\n");
        return (-1);
    }
    sfRenderWindow *window;
	sfVideoMode video_mode = {3000, 1200, 32};
    sfEvent event;
    sfTexture *texture;
    sfSprite  *sprite;
    sfClock *clock;
	sfTime time;
    sfVector2f size = {0.3, 0.3};
    sfVector2f pos = {0, 450};
    int x = 0;

    window = sfRenderWindow_create(video_mode, "My Hunter",
                sfDefaultStyle, NULL);
    texture = sfTexture_createFromFile("cars-clipart-turtle-16.png", NULL);
    sprite = sfSprite_create();
    clock = sfClock_create();

    sfSprite_setTexture(sprite, texture, sfTrue);
    sfSprite_setScale(sprite, size);
    while (sfRenderWindow_isOpen(window)) {
        sfSprite_setPosition(sprite, pos);
        sfRenderWindow_drawSprite(window, sprite, NULL);
        time = sfClock_getElapsedTime(clock);
        pos = sfSprite_getPosition(sprite);
        if (time.microseconds / 100000.0 > 0.5) {
            pos.x += atoi(av[1]);
            sfClock_restart(clock);
        }
        if (pos.x > video_mode.width)
            pos.x = 0;
        while (sfRenderWindow_pollEvent(window, &event)) {
            if (event.type == sfEvtClosed)
				sfRenderWindow_close(window);
        }
        sfRenderWindow_display(window);
        sfRenderWindow_clear(window, sfBlack);
    }

}