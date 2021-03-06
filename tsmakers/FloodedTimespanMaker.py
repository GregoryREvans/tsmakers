import abjad

from .TimespanMaker import TimespanMaker


class FloodedTimespanMaker(TimespanMaker):
    r"""
    A flooded timespan maker.

    ..  container:: example

        >>> timespan_maker = tsmakers.FloodedTimespanMaker()
        >>> print(abjad.storage(timespan_maker))
        tsmakers.FloodedTimespanMaker()

        >>> music_specifiers = {
        ...     'A': 'a music',
        ...     'B': 'b music',
        ... }
        >>> target_timespan = abjad.Timespan((1, 2), (2, 1))
        >>> timespan_list = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ... )
        >>> ts_list = abjad.TimespanList(
        ...     [
        ...         abjad.AnnotatedTimespan(
        ...             start_offset=_.start_offset,
        ...             stop_offset=_.stop_offset,
        ...             annotation=_.voice_name,
        ...         )
        ...         for _ in timespan_list
        ...     ]
        ... )
        >>> abjad.show(ts_list, scale=0.5, key="annotation") # doctest: +SKIP

        .. docs::

            >>> print(abjad.storage(timespan_list))
            abjad.TimespanList(
                [
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((2, 1)),
                        music_specifier='a music',
                        voice_name='A',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((2, 1)),
                        music_specifier='b music',
                        voice_name='B',
                        ),
                    ]
                )

    ..  container:: example

        >>> music_specifier = tsmakers.CompositeMusicSpecifier(
        ...     primary_music_specifier='one',
        ...     primary_voice_name='A',
        ...     rotation_indices=(0, 1, -1),
        ...     secondary_voice_name='B',
        ...     secondary_music_specifier=tsmakers.MusicSpecifierSequence(
        ...         application_rate='phrase',
        ...         music_specifiers=['two', 'three', 'four'],
        ...         ),
        ...     )
        >>> music_specifiers = {
        ...     'Performer Group': music_specifier,
        ...     }
        >>> timespan_list = timespan_maker(
        ...     music_specifiers=music_specifiers,
        ...     target_timespan=target_timespan,
        ...     )
        >>> ts_list = abjad.TimespanList(
        ...     [
        ...         abjad.AnnotatedTimespan(
        ...             start_offset=_.start_offset,
        ...             stop_offset=_.stop_offset,
        ...             annotation=_.voice_name,
        ...         )
        ...         for _ in timespan_list
        ...     ]
        ... )
        >>> abjad.show(ts_list, scale=0.5, key="annotation") # doctest: +SKIP

        .. docs::

            >>> print(abjad.storage(timespan_list))
            abjad.TimespanList(
                [
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((2, 1)),
                        music_specifier='one',
                        voice_name='A',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((2, 1)),
                        music_specifier='two',
                        voice_name='B',
                        ),
                    ]
                )

    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        division_masks=None,
        padding=None,
        seed=None,
        timespan_specifier=None,
    ):
        TimespanMaker.__init__(
            self,
            division_masks=division_masks,
            padding=padding,
            seed=seed,
            timespan_specifier=timespan_specifier,
        )

    ### PRIVATE METHODS ###

    def _make_timespans(
        self,
        layer=None,
        music_specifiers=None,
        target_timespan=None,
        timespan_list=None,
    ):
        start_offset = target_timespan.start_offset
        durations = [target_timespan.duration]
        new_timespans = abjad.TimespanList()
        for context_name, music_specifier in music_specifiers.items():
            timespans = music_specifier(
                durations=durations,
                layer=layer,
                division_masks=self.division_masks,
                padding=self.padding,
                seed=self.seed,
                start_offset=start_offset,
                timespan_specifier=self.timespan_specifier,
                voice_name=context_name,
            )
            new_timespans.extend(timespans)
        return new_timespans
