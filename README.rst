Parameters call function, :-)
=============================

You can do::

    from __future__ import print_function

    print('x', 'y', sep=',')

But I can not do::

    from __future__ import print_function

    parameters = ('x', 'y', sep=',')
    print(parameters)

With icall, I can do similar thing::

    from __future__ import print_function
    from icall import ICall

    parameters = ICall('x', 'y', sep=',')
    parameters(print)

Sometimes, you may use Parameters(similar to ICall)::

    from __future__ import print_function
    from icall import Parameters

    parameters = Parameters('x', 'y', sep=',')
    parameters(format)
