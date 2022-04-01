# ExaGen: Route generator for ExaBGP

Generates any number of IPv4 routes for advertisement via 
[ExaBGP](https://github.com/Exa-Networks/exabgp)

This simple script generates route announcements for ExaBGP to announce to its
peers. It is intended for testing routing table capacities and provide routes for
lab environments.

## Getting Started

1) Clone this repository

        git clone https://github.com/jvoss/ExaGen.git .

2) Install ExaBGP (if you do not already have it):

        pip install -r requirements.txt

2) Update your ExaBGP configuration with:

        process fullbgp {
            run python <full path to>/exagen.py <desired-next-hop-ip> <num_of_routes>;
            encoder text;
        }

    Example:

        process fullbgp {
            run python /home/user/ExaGen/exagen.py 192.168.1.1 200;
            encoder text;
        }
        
    See [sample.cfg](sample.cfg) for a simple complete ExaBGP configuration.

3) Run ExaBGP

    a) If running ExaBGP with minimal config, be sure to 
       set: `exabgp.api.ack=false`

        env exabgp.api.ack=false exabgp sample.cfg

## Contributing

Enhancements and bugfixes are encouraged. Please fork this project, make your
changes and submit a PR.
