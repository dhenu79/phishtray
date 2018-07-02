import React from 'react';
import { Route, Link } from 'react-router-dom';
import styled, { css } from 'react-emotion';

const Container = styled('div')(
  {
    padding: '30px',
    paddingLeft: '14px',
    borderLeft: '6px solid transparent',
  },
  props => ({
    backgroundColor: props.isSelected ? '#1C8BF4' : 'inherit',
    borderLeftColor: props.isSelected ? '#f4c760' : 'transparent',
  })
);

const Text = styled('div')(
  {
    color: '#fff',
    letterSpacing: '1.2px',
    textDecoration: 'none',
  },
  props => ({
    fontWeight: props.isSelected ? 'bold' : 'normal',
    opacity: props.isSelected ? 1 : 0.7,
  })
);

export default function AccountListItem({ account }) {
  return (
    <Route path={`/accounts/${account.id}`}>
      {({ match }) => (
        <Link
          to={`/accounts/${account.id}`}
          className={css({ textDecoration: 'none', display: 'block' })}
        >
          <Container isSelected={!!match}>
            <Text
              isSelected={!!match}
              className={css({
                fontSize: 18,
                lineHeight: '21px',
                marginBottom: 10,
              })}
            >
              {account.name}
            </Text>
          </Container>
        </Link>
      )}
    </Route>
  );
}
