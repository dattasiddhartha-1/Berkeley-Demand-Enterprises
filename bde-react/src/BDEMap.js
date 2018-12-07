import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import LocationOn from '@material-ui/icons/LocationOn'

const Store = (props) => {
    return (
        <LocationOn color='secondary' style={{ fontSize: 30 }}/>
    )
}

const BDEMap = (props) => {
    const defaultProps = {
        center: {
            lat: 40,
            lng: -102
        },
        zoom: 4
    };

    const stores = props.stores.map((store) => {
        return (
            <Store
                lat={store.lat}
                lng={store.lng}
            />
        )
    })

    return (
        <div style={{ height: '100vh', width: '100%' }}>
            <GoogleMapReact
                bootstrapURLKeys={{ key: 'AIzaSyAakDV-XUQ0XeH62DS0KH2Xnrx2K_LG3lM' }}
                defaultCenter={defaultProps.center}
                defaultZoom={defaultProps.zoom}
            >
                {stores}
            </GoogleMapReact>
        </div>
    );
}

export { BDEMap };
