import abjad
import quicktions


def divrewrite(tr, rulelst):
    rl = [rulelst]
    for nde in tr.levelorder:
        for rule in rl:
            if nde.value % rule[0] == 0:
                for val in rule[1]:
                    nde.insert_child(val)
    return TimespanTree()


def flatten(lst):
    out = []
    for i in lst:
        for x in i:
            out.extend([x])
    return out


def levelbylevel(root):
    out = []
    q = [root, None]
    while len(q) > 1:
        for i in q[: q.index(None)]:
            q.extend(i.children)
        out.append(q[: q.index(None)])
        del q[: q.index(None) + 1]
        q.extend([None])
    return out


def levelorder(root):
    out = []
    q = []
    q.append(root)
    while len(q) != 0:
        q.extend(q[0].children)
        out.append(q[0])
        q.pop(0)
    return out


def tally(lst):
    out = 0
    for i in lst:
        out += i
    return out


class TimespanTreeNode(object):
    def __init__(self, num=1, parent=None):
        self.value = num
        self.children = []
        self.parent = parent

    def insert_child(self, num):
        self.children.append(TimespanTreeNode(num, parent=self))

    def get_children(self):
        return self.children

    def get_childrensum(self):
        return tally([i.value for i in self.children])

    def get_number_of_children(self):
        return len(self.children)

    def get_parent(self):
        return self.parent

    def find_root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.find_root()

    def get_fract_value(self):
        if self.parent is None:
            return 1
        else:
            return quicktions.Fraction(self.value, self.parent.get_childrensum())

    def get_real_value(self):
        if self.parent is None:
            return self.value
        else:
            return self.get_fract_value() * self.parent.get_real_value()

    def localoffset(self):
        if self.parent is None:
            return 0
        else:
            return tally(
                [
                    i.get_real_value()
                    for i in self.parent.children[: self.parent.children.index(self)]
                ]
            )  # + self.localoffset()

    def offset(self):
        if self.parent is None:
            return 0
        else:
            return self.localoffset() + self.parent.offset()

    def get_timespan(self):
        if self.parent is None:
            return abjad.Timespan(0, self.value)
        else:
            return abjad.Timespan(self.offset(), self.offset() + self.get_real_value())


class TimespanTree(object):
    r"""

    ..  container:: example

        >>> a = tsmakers.TimespanTreeNode(10)
        >>> a.insert_child(1)
        >>> a.insert_child(1)
        >>> a.insert_child(1)
        >>> a.insert_child(1)
        >>> a.insert_child(1)
        >>> a.insert_child(1)
        >>> a.insert_child(1)
        >>> a.insert_child(1)
        >>> b, c, d, e, f, g, h, i = a.children
        >>> b.insert_child(2)
        >>> b.insert_child(1)
        >>> j, k = b.children
        >>> e.insert_child(3)
        >>> e.insert_child(1)
        >>> e.insert_child(2)
        >>> e.insert_child(2)
        >>> f.insert_child(1)
        >>> f.insert_child(1)
        >>> l, m = f.children
        >>> k.insert_child(1)
        >>> k.insert_child(1)
        >>> l.insert_child(1)
        >>> l.insert_child(1)
        >>> demotree = tsmakers.TimespanTree(a)
        >>> abjad.show(demotree.tspanlist()) # doctest: +SKIP

        ..  docs::

            >>> print(abjad.storage(demotree.tspanlist()))
            abjad.TimespanList(
                [
                    abjad.Timespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((10, 1)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((5, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((5, 4)),
                        stop_offset=abjad.Offset((5, 2)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((5, 2)),
                        stop_offset=abjad.Offset((15, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((15, 4)),
                        stop_offset=abjad.Offset((5, 1)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((5, 1)),
                        stop_offset=abjad.Offset((25, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((25, 4)),
                        stop_offset=abjad.Offset((15, 2)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((15, 2)),
                        stop_offset=abjad.Offset((35, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((35, 4)),
                        stop_offset=abjad.Offset((10, 1)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((5, 6)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((5, 6)),
                        stop_offset=abjad.Offset((5, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((15, 4)),
                        stop_offset=abjad.Offset((135, 32)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((135, 32)),
                        stop_offset=abjad.Offset((35, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((35, 8)),
                        stop_offset=abjad.Offset((75, 16)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((75, 16)),
                        stop_offset=abjad.Offset((5, 1)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((5, 1)),
                        stop_offset=abjad.Offset((45, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((45, 8)),
                        stop_offset=abjad.Offset((25, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((5, 6)),
                        stop_offset=abjad.Offset((25, 24)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((25, 24)),
                        stop_offset=abjad.Offset((5, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((5, 1)),
                        stop_offset=abjad.Offset((85, 16)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((85, 16)),
                        stop_offset=abjad.Offset((45, 8)),
                        ),
                    ]
                )

    ..  container:: example

        >>> a = tsmakers.TimespanTreeNode(10)
        >>> a.insert_child(8)
        >>> a.insert_child(5)
        >>> b, c,  = a.children
        >>> b.insert_child(8)
        >>> b.insert_child(5)
        >>> c.insert_child(8)
        >>> c.insert_child(5)
        >>> d, e,  = b.children
        >>> f, g,  = c.children
        >>> d.insert_child(8)
        >>> d.insert_child(5)
        >>> e.insert_child(8)
        >>> e.insert_child(5)
        >>> f.insert_child(8)
        >>> f.insert_child(5)
        >>> g.insert_child(8)
        >>> g.insert_child(5)
        >>> h, i,  = d.children
        >>> j, k,  = e.children
        >>> l, m,  = f.children
        >>> n, o,  = g.children
        >>> h.insert_child(8)
        >>> h.insert_child(5)
        >>> i.insert_child(8)
        >>> i.insert_child(5)
        >>> j.insert_child(8)
        >>> j.insert_child(5)
        >>> k.insert_child(8)
        >>> k.insert_child(5)
        >>> l.insert_child(8)
        >>> l.insert_child(5)
        >>> m.insert_child(8)
        >>> m.insert_child(5)
        >>> n.insert_child(8)
        >>> n.insert_child(5)
        >>> o.insert_child(8)
        >>> o.insert_child(5)
        >>> demotree = tsmakers.TimespanTree(a)
        >>> demotree_list = demotree.tspanlist()
        >>> demotree_list = demotree_list.round_offsets(
        ...     abjad.Duration((1, 8)),
        ...     anchor=abjad.Left,
        ... )
        ...
        >>> abjad.show(demotree_list, scale=0.7) # doctest: +SKIP

        ..  docs::

            >>> print(abjad.storage(demotree_list))
            abjad.TimespanList(
                [
                    abjad.Timespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((10, 1)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((49, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((49, 8)),
                        stop_offset=abjad.Offset((10, 1)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((15, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((15, 4)),
                        stop_offset=abjad.Offset((49, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((49, 8)),
                        stop_offset=abjad.Offset((17, 2)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((17, 2)),
                        stop_offset=abjad.Offset((10, 1)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((19, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((19, 8)),
                        stop_offset=abjad.Offset((15, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((15, 4)),
                        stop_offset=abjad.Offset((21, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((21, 4)),
                        stop_offset=abjad.Offset((49, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((49, 8)),
                        stop_offset=abjad.Offset((61, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((61, 8)),
                        stop_offset=abjad.Offset((17, 2)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((17, 2)),
                        stop_offset=abjad.Offset((75, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((75, 8)),
                        stop_offset=abjad.Offset((10, 1)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((0, 1)),
                        stop_offset=abjad.Offset((11, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((11, 8)),
                        stop_offset=abjad.Offset((19, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((19, 8)),
                        stop_offset=abjad.Offset((13, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((13, 4)),
                        stop_offset=abjad.Offset((15, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((15, 4)),
                        stop_offset=abjad.Offset((37, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((37, 8)),
                        stop_offset=abjad.Offset((21, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((21, 4)),
                        stop_offset=abjad.Offset((23, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((23, 4)),
                        stop_offset=abjad.Offset((49, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((49, 8)),
                        stop_offset=abjad.Offset((7, 1)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((7, 1)),
                        stop_offset=abjad.Offset((61, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((61, 8)),
                        stop_offset=abjad.Offset((65, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((65, 8)),
                        stop_offset=abjad.Offset((17, 2)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((17, 2)),
                        stop_offset=abjad.Offset((73, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((73, 8)),
                        stop_offset=abjad.Offset((75, 8)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((75, 8)),
                        stop_offset=abjad.Offset((39, 4)),
                        ),
                    abjad.Timespan(
                        start_offset=abjad.Offset((39, 4)),
                        stop_offset=abjad.Offset((10, 1)),
                        ),
                    ]
                )

    """

    def __init__(self, root):
        self.root = root
        self.levelorder = levelorder(root)
        self.levelbylevel = levelbylevel(root)

    def get_level_order(self):
        return self.levelorder

    def get_level(self, n):
        return self.levelbylevel[n]

    def get_level_order_value(self):
        return [[i.value for i in lev] for lev in self.levelbylevel]

    def get_level_value(self, n):
        return [i.value for i in self.levelbylevel[n]]

    def replace_values(self, lst):
        for i, j in zip(self.levelorder, lst):
            i.value = j

    def tspanlist_level(self, n):
        return abjad.TimespanList([i.get_timespan() for i in self.get_level(n)])

    def tspanlist(self):
        return abjad.TimespanList([i.get_timespan() for i in self.levelorder])

    def show(self):
        abjad.show(self.tspanlist(), scale=0.7)

    def show_level(self, n):
        abjad.show(self.tspanlist_level(n), scale=0.7)
