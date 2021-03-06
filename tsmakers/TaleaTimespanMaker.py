import collections

import abjad
from abjadext import rmakers

from .Cursor import Cursor
from .SilentTimespan import SilentTimespan
from .TimespanMaker import TimespanMaker


class TaleaTimespanMaker(TimespanMaker):
    r"""
    A talea timespan maker.

    ..  container:: example

        >>> timespan_maker = tsmakers.TaleaTimespanMaker(
        ...     initial_silence_talea=rmakers.Talea(
        ...         counts=(0, 4),
        ...         denominator=16,
        ...         )
        ...     )
        >>> print(abjad.storage(timespan_maker))
        tsmakers.TaleaTimespanMaker(
            initial_silence_talea=rmakers.Talea(
                [0, 4],
                16
                ),
            playing_talea=rmakers.Talea(
                [4],
                16
                ),
            playing_groupings=(1,),
            repeat=True,
            silence_talea=rmakers.Talea(
                [4],
                16
                ),
            step_anchor=Right,
            synchronize_groupings=False,
            synchronize_step=False,
            )

    ..  container:: example

        >>> import collections
        >>> music_specifiers = collections.OrderedDict([
        ...     ('A', None),
        ...     ('B', None),
        ...     ('C', None),
        ...     ('D', None),
        ...     ])
        >>> target_timespan = abjad.Timespan(0, 1)
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
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((1, 4)),
                        voice_name='A',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((1, 4)),
                        voice_name='C',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 4)),
                        stop_offset=abjad.Offset((1, 2)),
                        voice_name='B',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 4)),
                        stop_offset=abjad.Offset((1, 2)),
                        voice_name='D',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((3, 4)),
                        voice_name='A',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((3, 4)),
                        voice_name='C',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((3, 4)),
                        stop_offset=abjad.Offset((1, 1)),
                        voice_name='B',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((3, 4)),
                        stop_offset=abjad.Offset((1, 1)),
                        voice_name='D',
                        ),
                    ]
                )

    ..  container:: example

        >>> timespan_maker = abjad.new(timespan_maker,
        ...     initial_silence_talea=None,
        ...     synchronize_step=True,
        ...     )
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
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((1, 4)),
                        voice_name='A',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((1, 4)),
                        voice_name='B',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((1, 4)),
                        voice_name='C',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((1, 4)),
                        voice_name='D',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((3, 4)),
                        voice_name='A',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((3, 4)),
                        voice_name='B',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((3, 4)),
                        voice_name='C',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 2)),
                        stop_offset=abjad.Offset((3, 4)),
                        voice_name='D',
                        ),
                    ]
                )

    ..  container:: example

        >>> timespan_maker = abjad.new(timespan_maker,
        ...     initial_silence_talea=rmakers.Talea(
        ...         counts=(0, 2),
        ...         denominator=16,
        ...         ),
        ...     )
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
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((1, 4)),
                        voice_name='A',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((1, 4)),
                        voice_name='C',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 8)),
                        stop_offset=abjad.Offset((3, 8)),
                        voice_name='B',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((1, 8)),
                        stop_offset=abjad.Offset((3, 8)),
                        voice_name='D',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((5, 8)),
                        stop_offset=abjad.Offset((7, 8)),
                        voice_name='A',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((5, 8)),
                        stop_offset=abjad.Offset((7, 8)),
                        voice_name='C',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((3, 4)),
                        stop_offset=abjad.Offset((1, 1)),
                        voice_name='B',
                        ),
                    tsmakers.PerformedTimespan(
                        start_offset=abjad.Offset((3, 4)),
                        stop_offset=abjad.Offset((1, 1)),
                        voice_name='D',
                        ),
                    ]
                )

    ..  container:: example

        >>> music_specifiers = abjad.OrderedDict(
        ...     [(f"Voice {i+1}", None) for i in range(10)]
        ... )
        ...
        >>> target_timespan = abjad.Timespan(0, 8)
        >>> timespan_maker = tsmakers.TaleaTimespanMaker(
        ...     initial_silence_talea=rmakers.Talea(counts=([0, 5, 3, 6, 2]), denominator=8),
        ...     playing_talea=rmakers.Talea(counts=([5, 3, 1, 2, 6]), denominator=4),
        ...     playing_groupings=([1, 2, 3, 2]),
        ...     silence_talea=rmakers.Talea(counts=([5, 3, 4, 3]), denominator=4),
        ... )
        ...
        >>> temp_list = timespan_maker(
        ...     music_specifiers=music_specifiers, target_timespan=target_timespan
        ... )
        ...
        >>> t_list = abjad.TimespanList()
        >>> for span in temp_list:
        ...     new_span = abjad.AnnotatedTimespan(
        ...         span.start_offset,
        ...         span.stop_offset,
        ...         annotation=span.voice_name,
        ...     )
        ...     t_list.append(new_span)
        ...
        >>> def human_sorted_keys(pair):
        ...     key, timespan = pair
        ...     values = [to_digit(_) for _ in key.split()]
        ...     hashable_key = tuple(values)
        ...     return hashable_key
        ...
        >>> abjad.show(t_list, scale=0.5, key="annotation", sort_callable=human_sorted_keys) # doctest: +SKIP

        .. docs::

            >>> print(abjad.storage(t_list))
            abjad.TimespanList(
                [
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((5, 4)),
                        annotation='Voice 1',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((3, 2)),
                        annotation='Voice 6',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((1, 4)),
                        stop_offset=abjad.Offset((3, 4)),
                        annotation='Voice 5',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((1, 4)),
                        stop_offset=abjad.Offset((3, 2)),
                        annotation='Voice 10',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((3, 8)),
                        stop_offset=abjad.Offset((5, 8)),
                        annotation='Voice 3',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((3, 8)),
                        stop_offset=abjad.Offset((15, 8)),
                        annotation='Voice 8',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((5, 8)),
                        stop_offset=abjad.Offset((11, 8)),
                        annotation='Voice 2',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((5, 8)),
                        stop_offset=abjad.Offset((17, 8)),
                        annotation='Voice 7',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((3, 4)),
                        stop_offset=abjad.Offset((5, 4)),
                        annotation='Voice 4',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((3, 4)),
                        stop_offset=abjad.Offset((2, 1)),
                        annotation='Voice 9',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((3, 4)),
                        stop_offset=abjad.Offset((9, 4)),
                        annotation='Voice 5',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((5, 4)),
                        stop_offset=abjad.Offset((11, 4)),
                        annotation='Voice 4',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((11, 8)),
                        stop_offset=abjad.Offset((13, 8)),
                        annotation='Voice 2',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((3, 2)),
                        stop_offset=abjad.Offset((11, 4)),
                        annotation='Voice 6',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((13, 8)),
                        stop_offset=abjad.Offset((17, 8)),
                        annotation='Voice 2',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((15, 8)),
                        stop_offset=abjad.Offset((19, 8)),
                        annotation='Voice 3',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((2, 1)),
                        stop_offset=abjad.Offset((11, 4)),
                        annotation='Voice 9',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((17, 8)),
                        stop_offset=abjad.Offset((27, 8)),
                        annotation='Voice 7',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((19, 8)),
                        stop_offset=abjad.Offset((31, 8)),
                        annotation='Voice 3',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((5, 2)),
                        stop_offset=abjad.Offset((13, 4)),
                        annotation='Voice 1',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((21, 8)),
                        stop_offset=abjad.Offset((31, 8)),
                        annotation='Voice 8',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((11, 4)),
                        stop_offset=abjad.Offset((3, 1)),
                        annotation='Voice 9',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((11, 4)),
                        stop_offset=abjad.Offset((7, 2)),
                        annotation='Voice 10',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((25, 8)),
                        stop_offset=abjad.Offset((37, 8)),
                        annotation='Voice 2',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((13, 4)),
                        stop_offset=abjad.Offset((7, 2)),
                        annotation='Voice 1',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((27, 8)),
                        stop_offset=abjad.Offset((33, 8)),
                        annotation='Voice 7',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((7, 2)),
                        stop_offset=abjad.Offset((15, 4)),
                        annotation='Voice 10',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((7, 2)),
                        stop_offset=abjad.Offset((19, 4)),
                        annotation='Voice 5',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((15, 4)),
                        stop_offset=abjad.Offset((17, 4)),
                        annotation='Voice 9',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((15, 4)),
                        stop_offset=abjad.Offset((9, 2)),
                        annotation='Voice 6',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((15, 4)),
                        stop_offset=abjad.Offset((5, 1)),
                        annotation='Voice 4',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((31, 8)),
                        stop_offset=abjad.Offset((37, 8)),
                        annotation='Voice 8',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((17, 4)),
                        stop_offset=abjad.Offset((19, 4)),
                        annotation='Voice 1',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((17, 4)),
                        stop_offset=abjad.Offset((23, 4)),
                        annotation='Voice 9',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((9, 2)),
                        stop_offset=abjad.Offset((5, 1)),
                        annotation='Voice 10',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((37, 8)),
                        stop_offset=abjad.Offset((47, 8)),
                        annotation='Voice 2',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((37, 8)),
                        stop_offset=abjad.Offset((47, 8)),
                        annotation='Voice 3',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((19, 4)),
                        stop_offset=abjad.Offset((11, 2)),
                        annotation='Voice 5',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((19, 4)),
                        stop_offset=abjad.Offset((25, 4)),
                        annotation='Voice 1',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((5, 1)),
                        stop_offset=abjad.Offset((13, 2)),
                        annotation='Voice 10',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((21, 4)),
                        stop_offset=abjad.Offset((11, 2)),
                        annotation='Voice 6',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((43, 8)),
                        stop_offset=abjad.Offset((45, 8)),
                        annotation='Voice 7',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((11, 2)),
                        stop_offset=abjad.Offset((23, 4)),
                        annotation='Voice 5',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((11, 2)),
                        stop_offset=abjad.Offset((6, 1)),
                        annotation='Voice 6',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((45, 8)),
                        stop_offset=abjad.Offset((47, 8)),
                        annotation='Voice 8',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((45, 8)),
                        stop_offset=abjad.Offset((49, 8)),
                        annotation='Voice 7',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((23, 4)),
                        stop_offset=abjad.Offset((13, 2)),
                        annotation='Voice 4',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((47, 8)),
                        stop_offset=abjad.Offset((51, 8)),
                        annotation='Voice 8',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((47, 8)),
                        stop_offset=abjad.Offset((53, 8)),
                        annotation='Voice 3',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((25, 4)),
                        stop_offset=abjad.Offset((15, 2)),
                        annotation='Voice 1',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((51, 8)),
                        stop_offset=abjad.Offset((63, 8)),
                        annotation='Voice 8',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((13, 2)),
                        stop_offset=abjad.Offset((27, 4)),
                        annotation='Voice 4',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((13, 2)),
                        stop_offset=abjad.Offset((7, 1)),
                        annotation='Voice 5',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((13, 2)),
                        stop_offset=abjad.Offset((31, 4)),
                        annotation='Voice 10',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((53, 8)),
                        stop_offset=abjad.Offset((55, 8)),
                        annotation='Voice 3',
                        ),
                    abjad.AnnotatedTimespan(
                        start_offset=abjad.Offset((53, 8)),
                        stop_offset=abjad.Offset((59, 8)),
                        annotation='Voice 2',
                        ),
                    ]
                )

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        "_fuse_groups",
        "_initial_silence_talea",
        "_playing_talea",
        "_playing_groupings",
        "_reflect",
        "_repeat",
        "_silence_talea",
        "_step_anchor",
        "_synchronize_groupings",
        "_synchronize_step",
    )

    ### INITIALIZER ###

    def __init__(
        self,
        fuse_groups=None,
        initial_silence_talea=None,
        division_masks=None,
        padding=None,
        playing_talea=rmakers.Talea(
            counts=[4],
            denominator=16,
        ),
        playing_groupings=(1,),
        reflect=None,
        repeat=True,
        seed=None,
        silence_talea=rmakers.Talea(
            counts=[4],
            denominator=16,
        ),
        step_anchor=abjad.Right,
        synchronize_groupings=False,
        synchronize_step=False,
        timespan_specifier=None,
    ):
        TimespanMaker.__init__(
            self,
            division_masks=division_masks,
            padding=padding,
            seed=seed,
            timespan_specifier=timespan_specifier,
        )

        if fuse_groups is not None:
            fuse_groups = bool(fuse_groups)
        self._fuse_groups = fuse_groups

        if initial_silence_talea is not None:
            assert isinstance(initial_silence_talea, rmakers.Talea)
            assert initial_silence_talea.counts
            assert all(0 <= x for x in initial_silence_talea.counts)
        self._initial_silence_talea = initial_silence_talea

        assert isinstance(playing_talea, rmakers.Talea)
        assert playing_talea.counts
        assert all(0 < x for x in playing_talea.counts)
        self._playing_talea = playing_talea

        if not isinstance(playing_groupings, collections.Sequence):
            playing_groupings = (playing_groupings,)
        playing_groupings = tuple(int(x) for x in playing_groupings)
        assert len(playing_groupings)
        assert all(0 < x for x in playing_groupings)
        self._playing_groupings = playing_groupings

        if reflect is not None:
            reflect = bool(reflect)
        self._reflect = reflect

        self._repeat = bool(repeat)

        if silence_talea is not None:
            assert isinstance(silence_talea, rmakers.Talea)
            assert silence_talea.counts
            assert all(0 <= x for x in silence_talea.counts)
        self._silence_talea = silence_talea

        assert step_anchor in (abjad.Left, abjad.Right)
        self._step_anchor = step_anchor
        self._synchronize_groupings = bool(synchronize_groupings)
        self._synchronize_step = bool(synchronize_step)

    ### PRIVATE METHODS ###

    def _make_timespans(
        self,
        layer=None,
        music_specifiers=None,
        target_timespan=None,
        timespan_list=None,
    ):
        initial_silence_talea = self.initial_silence_talea
        if not initial_silence_talea:
            initial_silence_talea = rmakers.Talea(counts=(0,), denominator=1)
        initial_silence_talea = Cursor(initial_silence_talea)
        playing_talea = Cursor(self.playing_talea)
        playing_groupings = Cursor(self.playing_groupings)
        silence_talea = self.silence_talea
        if silence_talea is None:
            silence_talea = rmakers.Talea(counts=(0,), denominator=1)
        silence_talea = Cursor(silence_talea)

        if self.seed is not None and 0 < self.seed:
            for _ in range(self.seed):
                next(initial_silence_talea)
                next(playing_talea)
                next(playing_groupings)
                next(silence_talea)

        if self.synchronize_step:
            procedure = self._make_with_synchronized_step
        else:
            procedure = self._make_without_synchronized_step
        new_timespan_list, final_offset = procedure(
            initial_silence_talea=initial_silence_talea,
            layer=layer,
            playing_talea=playing_talea,
            playing_groupings=playing_groupings,
            music_specifiers=music_specifiers,
            silence_talea=silence_talea,
            target_timespan=target_timespan,
        )
        assert all(0 < _.duration for _ in new_timespan_list), (
            format(self),
            target_timespan,
        )

        if self.reflect:
            new_timespan_list = new_timespan_list.reflect(
                axis=target_timespan.axis,
            )

        return new_timespan_list

    def _make_with_synchronized_step(
        self,
        initial_silence_talea=None,
        layer=None,
        playing_talea=None,
        playing_groupings=None,
        music_specifiers=None,
        silence_talea=None,
        target_timespan=None,
    ):
        counter = collections.Counter()
        timespan_list = abjad.TimespanList()
        start_offset = target_timespan.start_offset
        stop_offset = target_timespan.stop_offset
        can_continue = True
        division_mask_seed = 0
        while start_offset < stop_offset and can_continue:
            silence_duration = next(silence_talea)
            durations = []
            if self.synchronize_groupings:
                grouping = next(playing_groupings)
                durations = [next(playing_talea) for _ in range(grouping)]
            for context_name, music_specifier in music_specifiers.items():
                if context_name not in counter:
                    counter[context_name] = 0
                seed = counter[context_name]
                initial_silence_duration = next(initial_silence_talea)
                if not self.synchronize_groupings:
                    grouping = next(playing_groupings)
                    durations = [next(playing_talea) for _ in range(grouping)]
                maximum_offset = (
                    start_offset
                    + sum(durations)
                    + silence_duration
                    + initial_silence_duration
                )
                # if self.padding:
                #    maximum_offset += (self.padding * 2)
                maximum_offset = min(maximum_offset, stop_offset)
                if self.step_anchor is abjad.Left:
                    maximum_offset = min(
                        maximum_offset,
                        (initial_silence_duration + start_offset + silence_duration),
                    )
                current_offset = start_offset + initial_silence_duration
                # if self.padding:
                #    current_offset += self.padding
                #    maximum_offset -= self.padding
                group_offset = current_offset

                valid_durations = []
                for duration in durations:
                    if maximum_offset < (current_offset + duration):
                        can_continue = False
                        break
                    valid_durations.append(duration)
                if self.fuse_groups:
                    valid_durations = [sum(valid_durations)]

                new_timespans = music_specifier(
                    durations=valid_durations,
                    layer=layer,
                    division_masks=self.division_masks,
                    padding=self.padding,
                    seed=seed,
                    division_mask_seed=division_mask_seed,
                    start_offset=group_offset,
                    timespan_specifier=self.timespan_specifier,
                    voice_name=context_name,
                )
                division_mask_seed += 1

                if all(isinstance(_, SilentTimespan) for _ in new_timespans):
                    new_timespans[:] = []
                timespan_list.extend(new_timespans)
                counter[context_name] += 1
            timespan_list.sort()
            if self.step_anchor == abjad.Right and timespan_list:
                start_offset = timespan_list.stop_offset
            start_offset += silence_duration
            if not self.repeat:
                break
        return timespan_list, start_offset

    def _make_without_synchronized_step(
        self,
        initial_silence_talea=None,
        layer=None,
        playing_talea=None,
        playing_groupings=None,
        music_specifiers=None,
        silence_talea=None,
        target_timespan=None,
    ):
        counter = collections.Counter()
        timespan_list = abjad.TimespanList()
        start_offset = target_timespan.start_offset
        stop_offset = target_timespan.stop_offset
        final_offset = abjad.Offset(0)
        for context_name, music_specifier in music_specifiers.items():

            if context_name not in counter:
                counter[context_name] = 0

            start_offset = target_timespan.start_offset
            start_offset += next(initial_silence_talea)
            can_continue = True

            while start_offset < stop_offset and can_continue:

                seed = counter[context_name]

                silence_duration = next(silence_talea)
                grouping = next(playing_groupings)
                durations = [next(playing_talea) for _ in range(grouping)]
                # if self.padding:
                #    start_offset += self.padding

                maximum_offset = start_offset + sum(durations) + silence_duration
                maximum_offset = min(maximum_offset, stop_offset)
                if self.step_anchor is abjad.Left:
                    maximum_offset = min(
                        maximum_offset, start_offset + silence_duration
                    )
                # if self.padding:
                #    maximum_offset -= self.padding

                group_offset = current_offset = start_offset

                valid_durations = []
                for duration in durations:
                    if maximum_offset < (current_offset + duration):
                        can_continue = False
                        break
                    valid_durations.append(duration)
                    current_offset += duration
                if len(durations) != len(valid_durations):
                    for _ in range(len(durations) - len(valid_durations)):
                        playing_talea.backtrack()
                if valid_durations and self.fuse_groups:
                    valid_durations = [sum(valid_durations)]

                new_timespans = music_specifier(
                    durations=valid_durations,
                    layer=layer,
                    division_masks=self.division_masks,
                    padding=self.padding,
                    seed=seed,
                    start_offset=group_offset,
                    timespan_specifier=self.timespan_specifier,
                    voice_name=context_name,
                )

                if all(isinstance(_, SilentTimespan) for _ in new_timespans):
                    new_timespans = []
                timespan_list.extend(new_timespans)

                if self.step_anchor is abjad.Left:
                    start_offset += silence_duration
                else:
                    start_offset = current_offset + silence_duration

                if stop_offset <= start_offset:
                    can_continue = False

                if not can_continue:
                    if not valid_durations:
                        silence_talea.backtrack()
                    silence_talea.backtrack()
                    playing_groupings.backtrack()

                if not self.repeat:
                    break
                counter[context_name] += 1
            if final_offset < start_offset:
                final_offset = start_offset
        return timespan_list, final_offset

    ### PUBLIC PROPERTIES ###

    @property
    def fuse_groups(self):
        return self._fuse_groups

    @property
    def initial_silence_talea(self):
        return self._initial_silence_talea

    @property
    def playing_groupings(self):
        return self._playing_groupings

    @property
    def playing_talea(self):
        return self._playing_talea

    @property
    def reflect(self):
        return self._reflect

    @property
    def repeat(self):
        return self._repeat

    @property
    def silence_talea(self):
        return self._silence_talea

    @property
    def step_anchor(self):
        return self._step_anchor

    @property
    def synchronize_groupings(self):
        return self._synchronize_groupings

    @property
    def synchronize_step(self):
        return self._synchronize_step
