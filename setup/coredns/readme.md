# if Mac OS create a dir
    sudo mkdir -p /etc/resolver && sudo sh -c 'echo "domain test\nnameserver 127.0.0.1\nsearch_order 1\ntimeout 5" > /etc/resolver/minikube-test'

# Flush the DNS Cache
    sudo dscacheutil -flushcache
    sudo killall -HUP mDNSResponder

# Restart the mDNSResponder Service
    sudo launchctl stop com.apple.mDNSResponder
    sudo launchctl start com.apple.mDNSResponder

# Verify the Changes
    scutil --dns