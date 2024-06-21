import csv


def read_rides_as_tuples(fname):
    """
    Read bus ride data as a list of tuples
    """

    records = []

    with open(fname) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip header

        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            record = (route, date, daytype, rides)
            records.append(record)

    return records


def read_rides_as_named_tuples(fname):
    """
    Read bus ride data as a list of named tuples
    """

    from collections import namedtuple

    Row = namedtuple("Row", ["route", "date", "daytype", "rides"])

    records = []

    with open(fname) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip header

        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            record = Row(route, date, daytype, rides)
            records.append(record)

    return records


def read_rides_as_dict(fname):
    """
    Read bus ride data as a dictionary
    """

    records = []

    with open(fname) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip header

        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            record = {
                "route": route,
                "date": date,
                "daytype": daytype,
                "rides": rides,
            }

            records.append(record)

    return records


def read_rides_as_class(fname):
    """
    Read bus ride data as a class
    """

    class Row:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []

    with open(fname) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip header

        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            record = Row(route, date, daytype, rides)

            records.append(record)

    return records


def read_rides_as_class_slotes(fname):
    """
    Read bus ride data as a class with __slotes__
    """

    class Row:
        __slots__ = ["route", "date", "daytype", "rides"]

        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []

    with open(fname) as f:
        rows = csv.reader(f)
        _ = next(rows)  # skip header

        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])

            record = Row(route, date, daytype, rides)
            records.append(record)

    return records


if __name__ == "__main__":
    import tracemalloc

    ## tuples
    tracemalloc.start()

    rows = read_rides_as_tuples("Data/ctabus.csv")

    print("Memory use: Current %d, Peak %d" % tracemalloc.get_traced_memory())

    tracemalloc.stop()

    ## named tuples
    tracemalloc.start()

    rows = read_rides_as_named_tuples("Data/ctabus.csv")

    print("Memory use: Current %d, Peak %d" % tracemalloc.get_traced_memory())

    tracemalloc.stop()

    ## dict
    tracemalloc.start()

    rows = read_rides_as_dict("Data/ctabus.csv")

    print("Memory use: Current %d, Peak %d" % tracemalloc.get_traced_memory())

    tracemalloc.stop()

    ## class
    tracemalloc.start()

    rows = read_rides_as_class("Data/ctabus.csv")

    print("Memory use: Current %d, Peak %d" % tracemalloc.get_traced_memory())

    tracemalloc.stop()

    ## class w slots
    tracemalloc.start()

    rows = read_rides_as_class_slotes("Data/ctabus.csv")

    print("Memory use: Current %d, Peak %d" % tracemalloc.get_traced_memory())

    tracemalloc.stop()
